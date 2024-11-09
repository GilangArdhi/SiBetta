import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image


# Load the saved model (architecture + weights)
model = load_model('./best_model_16.h5')
# Define class indices (for prediction)
# You can load these from a saved file or set them manually
class_indices = {
    'coccina': 0,
    'crown_tail': 1,
    'double_tail': 2,
    'halfmoon': 3,
    'halfsun': 4,
    'paradise': 5,
    'plakat': 6,
    'snakehead': 7,
    'spade_tail': 8,
    'veil_tail': 9
}

# Function to preprocess image for model prediction
def load_and_preprocess_image(img, target_size=(224, 224)):
    img = img.resize(target_size)  # Resize the image to 224x224 pixels
    img_array = image.img_to_array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize the image by scaling pixel values to [0, 1]
    return img_array

# Function to predict the image class
def predict_image_class(model, img, class_indices):
    img_array = load_and_preprocess_image(img)  # Preprocess image
    prediction = model.predict(img_array)  # Make prediction
    predicted_class = np.argmax(prediction, axis=1)  # Get the class with the highest score
    class_labels = {v: k for k, v in class_indices.items()}  # Reverse class_indices for label lookup
    confidence = prediction[0][predicted_class[0]]  # Get the probability of the predicted class
    return class_labels[predicted_class[0]], confidence  # Return predicted class and confidence



# Set background color for the header
st.markdown(
    """
    <style>
    .header {
        background-color: #0F52BA;
        padding: 20px;
        border-radius: 10px;
    }
    .header h1 {
        font-family: 'Arial Black', sans-serif;
        font-size: 50px;
        text-align: center;
    }
    .header p {
        text-align: center;
    }
    .upload-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        border: 2px dashed #CCCCCC;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section with background color
st.markdown(
    """
    <div class="header">
        <h1>SiBetta</h1>
        <p>Teman Setia Pecinta Cupang!</p>
        <p>Aplikasi web inovatif yang menggunakan teknologi AI untuk membantu Anda mengidentifikasi jenis ikan cupang dengan cepat dan mudah. 
        Aplikasi ini dirancang untuk pedagang ikan, pembeli ikan cupang, dan pecinta ikan cupang di seluruh Indonesia. 
        Ada 10 jenis ikan yang dapat dideteksi: coccina, crown tail, double tail, halfmoon, halfsun, paradise, plakat, snakehead, spade tail, veil tail</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("## Coba Sekarang!!!")
# Upload box for images
uploaded_file = st.file_uploader("Masukkan Gambar", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Gambar yang diunggah.', use_column_width=True)
        
    st.write("Mengolah gambar...")
    predicted_class, confidence = predict_image_class(model, img, class_indices)
    st.write(f'Hasil Prediksi: {predicted_class}')
    st.write(f'Tingkat Kemiripan: {confidence * 100:.2f}%')
    if predicted_class == 'paradise':
        st.markdown(
            """
            ## Keterangan Ikan Cupang Paradise
            Betta Paradise, juga dikenal sebagai Betta Macropodus "Paradise", adalah jenis ikan cupang hias yang populer dengan keindahannya yang luar biasa. Berikut adalah beberapa karakteristik utama Betta Paradise:

            ##Warna dan Pola:
            * **Warna:** Betta Paradise memiliki berbagai macam warna, termasuk merah, biru, hijau, ungu, dan kombinasi warna-warna tersebut. Warna mereka seringkali cerah dan berkilauan, dengan pola garis-garis, bintik-bintik, atau marmer yang unik.
            * **Sirip:** Sirip Betta Paradise panjang dan mengalir, terutama pada jantan. Sirip ini dapat memiliki berbagai warna dan pola, dan seringkali memiliki tepi yang halus atau berkilauan.
            
            ##Ukuran:
            * **Panjang:** Betta Paradise umumnya berukuran kecil, dengan panjang rata-rata sekitar 5 cm (2 inci) untuk jantan dan 4 cm (1,5 inci) untuk betina.
            * **Bentuk:** Tubuh Betta Paradise ramping dan memanjang, dengan kepala yang relatif besar.
            
            ##Temperamen:
            * **Jantan:** Betta Paradise jantan dikenal agresif terhadap ikan jantan lain, dan tidak boleh disimpan bersama dalam satu akuarium. Betina umumnya lebih damai, tetapi tetap dapat menunjukkan agresivitas terhadap satu sama lain.
            * **Betina:** Betta Paradise betina umumnya lebih damai daripada jantan, dan dapat hidup bersama dalam kelompok kecil.
            
            ##Perawatan:
            * **Akuarium:** Betta Paradise membutuhkan akuarium minimal 5 liter untuk satu jantan atau 10 liter untuk sekelompok betina. Akuarium harus dilengkapi dengan pemanas dan filter, dan airnya harus dijaga tetap bersih.
            * **Suhu:** Betta Paradise lebih menyukai air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Betta Paradise adalah karnivora dan membutuhkan makanan yang kaya akan protein. Mereka dapat diberi makan pelet ikan, cacing beku, dan udang air tawar.

            ## Sebagai gambaran umum, harga ikan cupang Paradise di Indonesia berkisar antara:
            * Rp 50.000 - Rp 100.000: Untuk ikan muda atau betina.
            * Rp 100.000 - Rp 200.000: Untuk ikan dewasa dengan kualitas standar.
            * Rp 200.000 - Rp 500.000: Untuk ikan dewasa dengan kualitas tinggi atau jenis yang langka.
            * Lebih dari Rp 500.000: Untuk ikan dengan kualitas luar biasa atau jenis yang sangat langka.
            """
        )
    elif predicted_class == 'crown_tail':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Crown Tail

            * **Sirip:** Sirip ekor cupang Crown Tail panjang dan mengalir, dengan tepi yang bergerigi atau berenda. Sirip ini menyerupai mahkota saat dikembang.
            * **Warna:** Cupang Crown Tail memiliki berbagai macam warna, termasuk merah, biru, hijau, ungu, dan hitam. Warna-warnanya seringkali cerah dan berkilauan.
            * **Ukuran:** Cupang Crown Tail adalah ikan cupang yang relatif kecil, dengan panjang tubuh sekitar 5 cm.
            * **Temperamen:** Cupang Crown Tail adalah ikan yang agresif, terutama terhadap jantan lain. Mereka tidak boleh dipelihara bersama ikan cupang jantan lainnya.
            * **Habitat:** Cupang Crown Tail berasal dari Asia Tenggara dan ditemukan di air tawar yang tenang, seperti sawah dan kolam.
            * **Perawatan:** Cupang Crown Tail membutuhkan akuarium yang kecil namun terawat dengan baik. Mereka membutuhkan air yang hangat dan bersih, serta banyak tempat untuk bersembunyi.

            ## Berikut adalah beberapa kategori harga ikan cupang Crown Tail di Indonesia:

            * Rp10.000 - Rp20.000: Ikan cupang Crown Tail muda atau betina dengan kualitas rendah.
            * Rp25.000 - Rp50.000: Ikan cupang Crown Tail dewasa atau jantan dengan kualitas rendah.
            * Rp50.000 - Rp100.000: Ikan cupang Crown Tail dengan kualitas sedang.
            * Rp100.000 - Rp250.000: Ikan cupang Crown Tail dengan kualitas tinggi.
            * Rp250.000 - Rp500.000: Ikan cupang Crown Tail dengan kualitas super tinggi, seperti yang memiliki garis keturunan juara atau yang telah memenangkan kontes.
            """
        )
    elif predicted_class == 'halfmoon':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Halfmoon

            Ikan cupang Halfmoon, yang terkenal dengan keindahannya, memiliki ciri khas yang membuatnya menonjol di antara jenis betta lainnya. Berikut beberapa karakteristik utama betta Halfmoon:

            ##Sirip Ekor yang Menakjubkan:
            * **Bentuk:** Ini adalah fitur yang paling menonjol. Sesuai namanya, sirip ekor Halfmoon berbentuk setengah lingkaran yang hampir sempurna, bisa mencapai sudut 180 derajat saat dikembangkan.
            * **Ukuran:** Sirip ekor Halfmoon sangat besar, seringkali melebihi ukuran tubuhnya. Ini membuat gerakan mereka anggun dan melambai saat berenang.
            
            ##Warna dan Pola:
            * **Warna:** Betta Halfmoon hadir dalam berbagai macam warna, seperti merah, biru, hijau, ungu, dan kombinasi warna-warna tersebut. Warnanya bisa solid, metalik, atau berpola seperti marmer.
            * **Sirip:** Sirip Halfmoon biasanya memiliki warna yang sama atau saling melengkapi dengan warna tubuh. Seringkali terdapat detail halus atau gradasi warna yang menambah keindahannya.
            
            ##Ukuran dan Bentuk Tubuh:
            * **Panjang:** Umumnya berukuran kecil hingga sedang, dengan panjang rata-rata 5-7 cm (2-2,7 inci) untuk jantan dan sedikit lebih pendek untuk betina.
            * **Bentuk:** Tubuh Halfmoon ramping dan memanjang, dengan kepala yang relatif besar.
            
            ##Temperamen:
            * **Jantan:** Mirip dengan betta lainnya, Halfmoon jantan dikenal agresif terhadap ikan jantan lain dari spesies yang sama. Mereka tidak boleh dipelihara bersama dalam satu akuarium.
            * **Betina:** Betina Halfmoon umumnya lebih damai daripada jantan, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ##Perawatan:
            * **Akuarium:** Betta Halfmoon membutuhkan minimal akuarium 5 liter untuk satu ekor. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Membutuhkan air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            ## Sebagai gambaran umum, harga Halfmoon di Indonesia berkisar antara:
            * Rp. 5.000 - Rp. 50.000: Untuk Halfmoon muda, betina, atau kualitas standar.
            * Rp. 50.000 - Rp. 150.000: Untuk Halfmoon dewasa dengan kualitas warna dan sirip yang bagus.
            * Rp. 150.000 - Rp. 500.000+ : Untuk Halfmoon kualitas premium, jenis langka, atau hasil breeding program khusus.
            """
        )
    elif predicted_class == 'halfsun':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Halfsun
            Betta Halfsun, juga dikenal sebagai Betta Macropodus "Combtail Halfmoon", adalah jenis ikan cupang hias yang populer dengan keindahannya yang unik. Berikut adalah beberapa karakteristik utama Betta Halfsun:

            ## Sirip Ekor yang Menawan:
            * **Bentuk:** Mirip Halfmoon, sirip ekor Halfsun berbentuk setengah lingkaran yang hampir sempurna.
            * **Ukuran:** Sirip ekornya besar, seringkali melebihi ukuran tubuh.
            * **Keunikan:** Ciri khasnya terletak pada ujung sirip ekor yang bergerigi menyerupai sisir, memberikan tampilan yang unik dan menarik.
            
            ## Warna dan Pola:
            * **Warna:** Betta Halfsun menampilkan berbagai warna, seperti merah, biru, hijau, ungu, dan kombinasi warna-warna tersebut. Warnanya bisa solid, metalik, atau berpola seperti marmer.
            * **Sirip:** Sirip Halfsun umumnya memiliki warna yang sama atau saling melengkapi dengan warna tubuh. Seringkali terdapat detail halus atau gradasi warna yang menambah keindahannya.
            
            ## Ukuran dan Bentuk Tubuh:
            * **Panjang:** Umumnya berukuran kecil hingga sedang, dengan panjang rata-rata 5-7 cm (2-2,7 inci) untuk jantan dan sedikit lebih pendek untuk betina.
            * **Bentuk:** Tubuh Halfsun ramping dan memanjang, dengan kepala yang relatif besar.
            
            ## Temperamen:
            * **Jantan:** Mirip dengan betta lainnya, Halfsun jantan dikenal agresif terhadap ikan jantan lain dari spesies yang sama. Mereka tidak boleh dipelihara bersama dalam satu akuarium.
            * **Betina:** Betina Halfsun umumnya lebih damai daripada jantan, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ## Perawatan:
            * **Akuarium:** Betta Halfsun membutuhkan minimal akuarium 5 liter untuk satu ekor. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Membutuhkan air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            ## Sebagai gambaran:
            * Rp. 20.000 - Rp. 50.000: Untuk Combtail muda, betina, atau kualitas standar.
            * Rp. 50.000 - Rp. 150.000: Untuk Combtail dewasa dengan kualitas warna dan sirip yang bagus.
            * Rp. 150.000 - Rp. 500.000+ : Untuk Combtail kualitas premium, jenis langka, atau hasil breeding program khusus.
            """
        )
    elif predicted_class == 'coccina':
        st.markdown(
            """
            ## Karakteristik Betta Coccina
            Betta Coccina, juga dikenal sebagai Betta Macropodus "Coccina", adalah spesies ikan cupang liar yang berasal dari Sumatera, Indonesia. Ikan ini terkenal dengan keindahannya yang unik dan memiliki beberapa ciri khas yang membedakannya dari jenis cupang lainnya. Berikut adalah beberapa karakteristik utama Betta Coccina:

            ## Ukuran dan Bentuk Tubuh:
            * **Panjang:** Betta Coccina tergolong ikan cupang kecil, dengan panjang rata-rata 4-5 cm (1,5-2 inci) untuk jantan dan 3-4 cm (1-1,5 inci) untuk betina.
            * **Bentuk:** Tubuh mereka ramping dan memanjang, dengan kepala yang relatif besar. Sirip punggung dan sirip dubur jantan panjang dan mengalir, sedangkan pada betina lebih pendek dan membulat.
            
            ## Warna dan Pola:
            * **Warna:** Betta Coccina umumnya memiliki warna merah cerah, dengan corak coklat atau hitam di bagian atas tubuh. Betina berwarna lebih pucat dengan bintik-bintik merah.
            * **Pola:** Pola pada Betta Coccina bervariasi, namun yang paling umum adalah pola garis-garis vertikal di bagian samping tubuh.
            
            ## Sirip Ekor:
            * **Bentuk:** Sirip ekor Betta Coccina jantan berbentuk kipas, sedangkan pada betina lebih pendek dan membulat.
            * **Warna:** Sirip ekor umumnya berwarna merah dengan tepi hitam atau biru.
            
            ## Temperamen:
            * **Jantan:** Seperti jenis cupang lainnya, Betta Coccina jantan sangat agresif terhadap jantan lain.
            * **Betina:** Betina umumnya lebih damai, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ## Perawatan:
            * **Akuarium:** Betta Coccina membutuhkan minimal akuarium 5 liter untuk satu ekor jantan atau 10 liter untuk sekelompok betina. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Betta Coccina menyukai air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            ## Sebagai gambaran:
            * Rp 35.000 - Rp 100.000: Untuk Betta Coccina muda, betina, atau kualitas standar.
            * Rp 100.000 - Rp 200.000: Untuk Betta Coccina dewasa dengan kualitas warna dan sirip yang bagus.
            * Rp 200.000 - Rp 500.000+ :** Untuk Betta Coccina kualitas premium, jenis langka, atau hasil breeding program khusus.
            """
        )
    elif predicted_class == 'double_tail':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Double Tail
            
            Betta double tail, yang juga dikenal dengan sebutan DT (doubletail male), DTF (doubletail female), atau DTM (doubletail male), adalah ikan cupang hias yang menawan dengan ciri khas pada bagian ekornya. Berikut adalah beberapa karakteristik utama betta double tail:

            ## Ekor Bercabang:
            * **Bentuk:** Ini adalah fitur yang paling menonjol. Ekornya terbelah menjadi dua lobus yang terpisah hingga pangkal, sehingga tampak seperti memiliki dua ekor.
            * **Kesempurnaan:** Idealnya, belahan ekor pada betta double tail simetris dan memiliki panjang yang sama.
            
            ## Sirip Lainnya:
            * **Sirip Punggung (Dorsal Fin):** Biasanya lebih panjang dari betta plakat pada umumnya, bahkan bisa menyamai panjang sirip anal.
            * **Sirip Anal (Anal Fin):** Umumnya berukuran normal dan selaras dengan sirip punggung.
            
            ## Warna dan Pola:
            * **Variasi Warna:** Betta double tail hadir dalam berbagai macam warna, sama seperti betta jenis lainnya. Mereka bisa berwarna merah, biru, hijau, ungu, atau kombinasi dari warna-warna tersebut. Warnanya bisa solid, metalik, atau berpola seperti marmer.
            * **Kesesuaian Warna:** Umumnya sirip dan tubuh betta double tail memiliki warna yang senada atau saling melengkapi. Seringkali terdapat detail halus atau gradasi warna yang menambah keindahannya.
            
            ## Ukuran dan Bentuk Tubuh:
            * **Panjang:** Umumnya berukuran kecil hingga sedang, dengan panjang rata-rata 5-7 cm (2-2,7 inci) untuk jantan dan sedikit lebih pendek untuk betina.
            * **Bentuk:** Tubuh betta double tail ramping dan memanjang, dengan kepala yang relatif besar.
            
            ## Temperamen:
            * **Jantan:** Mirip dengan betta lainnya, jantan double tail dikenal agresif terhadap ikan jantan lain dari spesies yang sama. Mereka tidak boleh dipelihara bersama dalam satu akuarium.
            * **Betina:** Betina double tail umumnya lebih damai daripada jantan, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ## Perawatan:
            * **Akuarium:** Betta double tail membutuhkan minimal akuarium 5 liter untuk satu ekor. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Membutuhkan air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            Sebagai gambaran umum, harga betta double tail di Indonesia berkisar antara:
            * Rp. 50.000 - Rp. 150.000: Untuk betta double tail muda, betina, atau kualitas standar.
            * Rp. 150.000 - Rp. 300.000: Untuk betta double tail dewasa dengan kualitas warna dan sirip yang bagus.
            * Rp. 300.000 - Rp. 1.000.000+: Untuk betta double tail kualitas premium, warna langka, atau hasil breeding program khusus.
            """
        )
    elif predicted_class == 'snakehead':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Snakehead
            Betta snakehead, juga dikenal dengan nama ilmiah Betta channoides, bukanlah cupang hias yang biasa ditemukan di toko ikan. Mereka adalah ikan cupang liar yang berasal dari Asia Tenggara,  memiliki beberapa perbedaan mendasar dengan cupang hias pada umumnya. Berikut adalah beberapa karakteristik utama betta snakehead:

            ## Bentuk Tubuh:
            * **Panjang:** Betta snakehead umumnya berukuran lebih besar daripada cupang hias, dengan panjang rata-rata mencapai 12 cm (4,7 inci)
            * ** ramping dan memanjang:** Mirip dengan cupang hias, tetapi tubuhnya cenderung lebih ramping dan memanjang.
            * **Kepala Besar:** Mereka memiliki kepala yang lebih besar dan mulut yang lebar dibandingkan cupang hias.
            
            ## Sirip:
            * **Sirip Punggung dan Sirip Dubur:** Cenderung lebih pendek dan kurang mengalir dibandingkan cupang hias plakat atau halfmoon.
            * **Sirip Ekor:** Berbentuk membulat dan tidak memanjang seperti kebanyakan cupang hias.
            
            ## Warna dan Pola:
            * **Warna Dasar:** Umumnya berwarna coklat kemerahan atau keabu-abuan.
            * **Pola:** Biasanya memiliki pola garis-garis vertikal di sepanjang tubuh, terkadang dengan bintik-bintik atau corak samar lainnya.
            
            ## Pernapasan Atmosfer:
            * **Labirin Organ:** Betta snakehead memiliki organ labirin yang memungkinkan mereka mengambil oksigen langsung dari udara. Ini merupakan ciri khas yang tidak dimiliki oleh cupang hias pada umumnya.
            
            ##Temperamen:
            * **Agresif:** Betta snakehead dikenal sangat agresif terhadap ikan lain, termasuk sesama betta snakehead. Mereka tidak cocok untuk dipelihara bersama ikan lain dalam satu akuarium.
            
            Perawatan:
            * **Tidak Umum dipelihara:** Betta snakehead bukanlah ikan yang umum dipelihara sebagai ikan hias. Mereka membutuhkan perawatan khusus dan akuarium yang lebih besar dibandingkan cupang hias pada umumnya.

            ## Menjual dan memelihara ikan Betta channoides (Betta snakehead) sebagai ikan hias  dapat menimbulkan kontroversi di Indonesia.  Berikut beberapa alasannya:
            * **Regulasi:** Beberapa daerah di Indonesia mungkin memiliki peraturan yang melarang kepemilikan atau perdagangan ikan predator seperti Betta channoides.
            * **Invasif:** Betta channoides berpotensi menjadi spesies invasif jika dilepaskan ke habitat liar. Mereka bisa mengganggu keseimbangan ekosistem dengan memangsa ikan asli.
            * **Perawatan:** Betta channoides membutuhkan perawatan khusus dan akuarium yang lebih besar dibandingkan cupang hias pada umumnya.
            Karena faktor-faktor tersebut,  Anda mungkin kesulitan menemukan Betta snakehead dijual secara terbuka di toko ikan hias Indonesia.

            ## Alternatif lain:
            * **Ikan cupang hias:** Jika Anda tertarik pada keindahan ikan cupang, ada banyak sekali jenis cupang hias yang cantik dan aman dipelihara, seperti Betta splendens (cupang plakat, halfmoon, dll).
            * **Informasi online:** Anda bisa mencari informasi tentang Betta channoides secara online melalui website atau forum pecinta ikan hias. Pastikan sumber informasinya kredibel.
            """
        )
    elif predicted_class == 'spade_tail':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Spade Tail
            Betta spade tail, atau yang dikenal dengan sebutan cupang ekor sekop, adalah salah satu jenis ikan cupang hias yang menarik. Mereka memiliki ciri khas pada bentuk ekornya yang menyerupai sekop kartu remi, sehingga dinamakan demikian. Berikut adalah beberapa karakteristik utama betta spade tail:

            ## Sirip Ekor Berbentuk Sekop:
            * **Bentuk:** Ini adalah fitur yang paling menonjol. Ekornya memanjang ke belakang, namun bagian ujungnya melebar dan meruncing ke satu titik, menyerupai bentuk sekop.
            * **Panjang:** Sirip ekor betta spade tail umumnya panjang dan melebihi ukuran tubuhnya.
            * **Kesempurnaan:** Idealnya, kedua belahan ekor pada betta spade tail simetris dan ujungnya meruncing dengan tajam.
            
            ## Sirip Lainnya:
            * **Sirip Punggung (Dorsal Fin):** Biasanya berukuran sedang, tidak sepanjang sirip punggung pada jenis plakat atau halfmoon.
            * **Sirip Anal (Anal Fin):** Umumnya berukuran selaras dengan sirip punggung.
            
            ## Warna dan Pola:
            * **Variasi Warna:** Betta spade tail hadir dalam berbagai macam warna, sama seperti betta jenis lainnya. Mereka bisa berwarna merah, biru, hijau, ungu, atau kombinasi dari warna-warna tersebut. Warnanya bisa solid, metalik, atau berpola seperti marmer.
            * **Kesesuaian Warna:** Umumnya sirip dan tubuh betta spade tail memiliki warna yang senada atau saling melengkapi. Seringkali terdapat detail halus atau gradasi warna yang menambah keindahannya.
            
            ## Ukuran dan Bentuk Tubuh:
            * **Panjang:** Umumnya berukuran kecil hingga sedang, dengan panjang rata-rata 5-7 cm (2-2,7 inci) untuk jantan dan sedikit lebih pendek untuk betina.
            * **Bentuk:** Tubuh betta spade tail ramping dan memanjang, dengan kepala yang relatif besar.
            
            ## Temperamen:
            * **Jantan:** Mirip dengan betta lainnya, jantan spade tail dikenal agresif terhadap ikan jantan lain dari spesies yang sama. Mereka tidak boleh dipelihara bersama dalam satu akuarium.
            * **Betina:** Betina spade tail umumnya lebih damai daripada jantan, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ## Perawatan:
            * **Akuarium:** Betta spade tail membutuhkan minimal akuarium 5 liter untuk satu ekor. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Membutuhkan air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            Sebagai gambaran umum, harga betta spade tail di Indonesia berkisar antara:
            * Rp. 500.000 - Rp. 1.000.000: Untuk betta spade tail muda, betina, atau kualitas standar.
            * Rp. 1.000.000 - Rp. 2.000.000: Untuk betta spade tail dewasa dengan kualitas warna dan sirip yang bagus.
            * Rp. 2.000.000 - Rp. 5.000.000+: Untuk betta spade tail kualitas premium, warna langka, atau hasil breeding program khusus.
            """
        )
    elif predicted_class == 'veil_tail':
        st.markdown(
            """
            ## Karakteristik Ikan Cupang Halfsun
            
            Betta veil tail, yang sering disebut cupang ekor veil atau cupang ekor panjang, adalah salah satu jenis ikan cupang hias yang populer dengan keindahan siripnya yang panjang dan mengalir. Berikut adalah beberapa karakteristik utama betta veil tail:

            ## Sirip Ekor Panjang dan Flowing:
            * **Panjang:** Ini adalah fitur yang paling menonjol. Sirip ekornya memanjang melebihi ukuran tubuh, terkadang mencapai 2-3 kali panjang tubuhnya.
            * **Bentuk:** Alih-alih meruncing ke satu titik seperti pada plakat atau berbentuk bulan sabit seperti pada halfmoon, sirip ekor veil tail menjuntai ke bawah dan melebar di bagian ujungnya, menyerupai kerudung atau veil (penutup kepala wanita).
            Gerakan:** Saat berenang, sirip ekor veil tail akan bergerak anggun dan mengalir, menambah kesan elegan pada ikan ini.
            
            ## Sirip Lainnya:
            Sirip Punggung (Dorsal Fin):** Umumnya berukuran panjang dan selaras dengan sirip ekor, namun tidak melebihi panjang tubuh.
            Sirip Anal (Anal Fin):** Memiliki panjang yang selaras dengan sirip punggung, menciptakan keseimbangan visual.
            Sirip Dada (Pectoral Fins):** Berukuran sedang dan tidak terlalu mencolok.
            
            ## Warna dan Pola:
            Variasi Warna:** Betta veil tail hadir dalam berbagai macam warna, sama seperti betta jenis lainnya. Mereka bisa berwarna merah, biru, hijau, ungu, atau kombinasi dari warna-warna tersebut. Warnanya bisa solid, metalik, atau berpola seperti marmer.
            Kesesuaian Warna:** Umumnya sirip dan tubuh betta veil tail memiliki warna yang senada atau saling melengkapi. Seringkali terdapat detail halus atau gradasi warna yang menambah keindahannya.
            
            ## Ukuran dan Bentuk Tubuh:
            * **Panjang:** Umumnya berukuran kecil hingga sedang, dengan panjang rata-rata 5-7 cm (2-2,7 inci) untuk jantan dan sedikit lebih pendek untuk betina.
            * **Bentuk:** Tubuh betta veil tail ramping dan memanjang, dengan kepala yang relatif besar.
            
            Temperamen:
            * **Jantan:** Mirip dengan betta lainnya, jantan veil tail dikenal agresif terhadap ikan jantan lain dari spesies yang sama. Mereka tidak boleh dipelihara bersama dalam satu akuarium.
            * **Betina:** Betina veil tail umumnya lebih damai daripada jantan, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ## Perawatan:
            * **Akuarium:** Betta veil tail membutuhkan minimal akuarium 5 liter untuk satu ekor. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Membutuhkan air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            ## Sebagai gambaran umum, harga betta veil tail di Indonesia berkisar antara:
            * Rp. 50.000 - Rp. 100.000: Untuk betta veil tail muda, betina, atau kualitas standar.
            * Rp. 100.000 - Rp. 200.000: Untuk betta veil tail dewasa dengan kualitas warna dan sirip yang bagus.
            * Rp. 200.000 - Rp. 500.000+: Untuk betta veil tail kualitas premium, warna langka, atau hasil breeding program khusus.
            """
        )
    elif predicted_class == 'plakat':
        st.markdown(
            """
            ## Karakteristik Betta Plakat
            Betta plakat, yang juga dikenal sebagai cupang plakat, adalah salah satu jenis ikan cupang hias yang populer di Indonesia. Mereka terkenal dengan sifatnya yang agresif dan sirip ekornya yang pendek dan tebal. Berikut adalah beberapa karakteristik utama betta plakat:

            ## Sirip Ekor Pendek dan Tebal:
            * **Panjang:** Sirip ekor betta plakat umumnya berukuran pendek, hanya sekitar setengah panjang tubuhnya.
            * **Bentuk:** Ekornya berbentuk seperti kipas atau daun, dengan tepi yang rata atau sedikit melengkung.
            * **Tekstur:** Sirip ekor plakat terasa lebih tebal dan kaku dibandingkan jenis cupang lain.
            
            ## Sirip Lainnya:
            * **Sirip Punggung (Dorsal Fin):** Berukuran lebih panjang dan tegak dibandingkan sirip ekor, dengan bentuk yang runcing atau membulat.
            * **Sirip Anal (Anal Fin):** Memiliki panjang yang selaras dengan sirip punggung, menciptakan keseimbangan visual.
            * **Sirip Dada (Pectoral Fins):** Berukuran sedang dan tidak terlalu mencolok.
            
            ## Warna dan Pola:
            * **Variasi Warna:** Betta plakat hadir dalam berbagai macam warna, sama seperti betta jenis lainnya. Mereka bisa berwarna merah, biru, hijau, ungu, atau kombinasi dari warna-warna tersebut. Warnanya bisa solid, metalik, atau berpola seperti marmer.
            * **Kesesuaian Warna:** Umumnya sirip dan tubuh betta plakat memiliki warna yang senada atau saling melengkapi. Seringkali terdapat detail halus atau gradasi warna yang menambah keindahannya.
            
            ## Ukuran dan Bentuk Tubuh:
            * **Panjang:** Umumnya berukuran kecil hingga sedang, dengan panjang rata-rata 5-7 cm (2-2,7 inci) untuk jantan dan sedikit lebih pendek untuk betina.
            * **Bentuk:** Tubuh betta plakat ramping dan memanjang, dengan kepala yang relatif besar.
            
            ## Temperamen:
            * **Jantan:** Betta plakat terkenal dengan sifatnya yang agresif, terutama terhadap ikan jantan lain dari spesies yang sama. Mereka tidak boleh dipelihara bersama dalam satu akuarium.
            * **Betina:** Betina plakat umumnya lebih damai daripada jantan, tetapi tetap disarankan untuk dipelihara sendiri atau dalam kelompok kecil dengan jenis ikan lain yang kompatibel.
            
            ## Perawatan:
            * **Akuarium:** Betta plakat membutuhkan minimal akuarium 5 liter untuk satu ekor. Akuarium harus dilengkapi dengan pemanas dan filter, serta air yang dijaga kebersihannya.
            * **Suhu:** Membutuhkan air hangat dengan suhu antara 24°C hingga 27°C (75°F hingga 81°F).
            * **Makanan:** Mereka adalah karnivora dan membutuhkan makanan berprotein tinggi seperti pelet ikan, cacing beku, dan udang air tawar.

            ## Sebagai gambaran umum, harga betta plakat di Indonesia berkisar antara:
            * Rp. 10.000 - Rp. 50.000: Untuk betta plakat muda, betina, plakat biasa, atau kualitas standar.
            * Rp. 50.000 - Rp. 200.000: Untuk betta plakat dewasa dengan kualitas warna dan sirip yang bagus, plakat koi, atau plakat halfmoon.
            * Rp. 200.000 - Rp. 1.000.000+: Untuk betta plakat plakat giant, plakat lukisan, atau hasil breeding program khusus.
            """
        )
    # ... Add similar else if statements for each class in class_indices
    else:
        st.write('Deskripsi untuk kelas ini belum tersedia.')
