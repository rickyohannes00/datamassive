import re
from collections import Counter
from heapq import nlargest
from textblob import TextBlob  # Untuk analisis sentimen

def analyze_sentiment(text):
    # Menggunakan TextBlob untuk menganalisis sentimen
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiment_label = "Positif"
    elif sentiment < 0:
        sentiment_label = "Negatif"
    else:
        sentiment_label = "Netral"
    return sentiment_label, sentiment

def summarize_text(text, max_sentences=3):
    # Step 1: Text Preprocessing
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split sentences using punctuation
    words = re.findall(r'\w+', text.lower())  # Extract words and normalize to lowercase
    
    # Step 2: Calculate Word Frequencies
    word_frequencies = Counter(words)
    max_frequency = max(word_frequencies.values())  # Normalize word frequencies
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    # Step 3: Sentence Scoring
    sentence_scores = {}
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):  # Tokenize sentence
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

    # Step 4: Select Top Sentences
    top_sentences = nlargest(max_sentences, sentence_scores, key=sentence_scores.get)
    
    # Combine selected sentences into the final summary
    summary = " ".join(top_sentences)
    return summary

def get_most_frequent_words(text, n=10):
    # Mengambil kata yang paling sering muncul
    words = re.findall(r'\w+', text.lower())
    word_frequencies = Counter(words)
    most_common = nlargest(n, word_frequencies.items(), key=lambda x: x[1])
    return most_common

# Contoh penggunaan
text1 = """Assalamualaikum wr wb

Yang saya banggakan, saya hormati, ketua dan seluruh anggota KPU beserta seluruh jajaran. Yang saya muliakan, saya banggakan, para ketua umum-ketua umum partai-partai politik beserta sekjen dan seluruh jajaran, yang saya banggakan para pasangan calon presiden dan calon wakil presiden yang saya hormati.
Saya diperintah oleh calon presiden untuk mewakili kami berdua, atas nama AMIN untuk Indonesia.
Puji syukur alhamdulillah, hari ini kita sampai pada tahapan yang sangat penting, dimulainya proses pemilihan umum, dengan penetapan dan penentuan nomor urut pada malam hari ini.
Alhamdulillah, kita bersyukur semua proses berjalan lancar dan kita menyaksikan KPU bekerja secara profesional, tepuk tangan untuk KPU.
Yang kedua, kita juga sangat berbahagia dan bersyukur bahwa akhirnya masing-masing calon presiden dan calon wakil presiden, telah menyiapkan diri dengan baik, sehingga kita sampai pada satu tahap, berkomitmen untuk melaksanakan pemilu dengan semangat penuh riang gembira dan sekaligus kita ingin bersama-sama mengisi pemilu dengan gagasan, ide, cita-cita, dimulai dari track record, rekam jejak dan berbagai visi misi yang telah kita miliki masing-masing secara lengkap.
Alhamdulillah, hari ini Timnas pemenangan AMIN saya laporkan kepada seluruh rakyat bangsa Indonesia telah siap mengikuti kompetisi dengan sehat dan sportif.
AMIN menganggap bahwa kita telah miliki kesempatan untuk terus menjaga agar pemilihan umum berjalan dengan langsung, umum, bebas, dan rahasia, dilaksanakan dengan penuh kejujuran, keterbukaan, dan kebersamaan.
Kepada seluruh masyarakat, rakyat, Bangsa Indonesia, lihatlah pemilu ini ibarat seperti kompetisi pertandingan sepak bola. Kita ingin menyaksikan tim masing-masing capres dan cawapres bermain secara sportif, dan bermain secara terbuka, sehingga ibaratnya rakyat harus menikmati pemilu tahun ini dengan penuh riang gembira dan kebersamaan, serta kekeluargaan, berkompetisi tetapi tetap berkeluarga dan bersaudara. Aamiin
Kita semua yakin kalau kita melihat pemilu seperti sepak bola, maka rakyat punya kesempatan untuk menyaksikan dengan bahagia. Kalau ada pemain yang bersifat curang, tolong diteriaki supaya tidak curang. Kalau ada wasit merangkap pemain, kita foto dan kita sebarluaskan. Kalau ada wasit yang curang, kita laporkan kepada FIFA sebagai lembaga tertinggi. Kalau ada pemain yang nakal dan nackling lawan, foto dan viralkan ke seluruh penjuru.
Itulah pemilu yang saling menjaga. Karena apa, pemilu adalah taruhan bangsa kita. Kalau pemilu berjalan dengan baik, legitimate, objektif, insyaallah negeri ini akan tetap bersatu, kuat, dan berhasil membangun. Kalau pemilu ini berjalan dengan jujur dan adil, insyaallah pembangunan akan lancar selancar-lancarnya
Ke Mamuju jangan lupa pakai sepatu
Kalau ingin maju, pilihlah nomor satu
Oleh karena itu, mari kita semua seluruh rakyat bangsa Indonesia mengikuti pemilihan umum dengan semangat membangun bangsa, dengan semangat menjaga momentum demokrasi yang telah kita jaga dan berhasil hingga hari ini. Kita tidak ingin demokrasi mundur ke belakang dan tanpa arah yang jelas, aamiin.
Karena itu, saya dan Mas Anies bersyukur kita dapat nomor satu, pertanda baik. Amin nomor 1. Selamat kepada seluruh bangsa Indonesia, mari kita bersama-sama menjaga pemilihan umum dengan penuh semangat, penuh kekeluargaan, sportif, beradu gagasan, beradu cita-cita, beradu cara kerja, insyaallah alhamdulillah...
Indonesia semakin kuat dan kokoh bagi keadilan dan kemakmuran, yang ingin perubahan, jangan lupa nomor 1."""  #Pidato paslon pertama
text2 = """Assalamualaikum Warahmatullahi Wabarakatuh

Salam sejahtera bagi kita sekalian, Shalom, Om swastiastu, Namo buddhaya, Salam kebajikan
Yang saya hormati dan saya banggakan Bawaslu, Ketua DKPP dan semua unsur yang telah mendukung proses dahap demi tahap pemilihan umum,
Ketua umum partai-partai politik yang hadir. Presiden Republik Indonesia ke-5 yang saya hormati beserta seluruh ketua, sekjen partai-partai politik, kemudian juga pasangan calon nomor satu dan nomor tiga yang saya hormati dan saya banggakan.
Tentunya kita bersyukur kehadirat Allah SWT, Tuhan Maha Besar, kita diberi kesehatan dapat mengikuti acara yang demikian penting secara baik dan sempurna. Saya atas nama pasangan calon nomor dua mengucapkan terima kasih dan penghargaan setinggi-tingginya kepada KPU kemudian juga kepada Bawaslu dan DKPP atas terselenggranya proses pemilihan umum dengan baik.
Saya tidak akann panjang lebar pidato, tapi Saya ingin sampaikan di sini bahwa kita patut bangga kita adalah negara demokrasi, salah satu yang terbesar di dunia, kalau tidak salah ketiga terbesar di dunia, dan kita telah mengalami pemilihan umum periode demi periode dan kita bersyukur bahwa negara kita masih utuh masih bersatu walaupun begitu banyak tantangan yang dihadapi
Saya sangat setuju dengan tadi aspirasi dan harapan yang disampaikan oleh pasangan calon nomor satu, kalau baik kita katakan baik, kejujuran itu harus utuh, seutuh-utuhnya.
Jadi saya sangat sependapat dengan aspirasi pasangan calon nomor 1, memang kita bersyukur kita memiliki negara berdemokrasi, kita percaya dan yakin KPU akan melaksanakan semua proses pemilu dengan sebaik-baiknya, dengan sejujur-jujurnya, dengan seadil-adilnya, tanpa kecurangan apapupn, karena kalau melaksanakan pemilu yang curang menghianati bangsa dan rakyat Indonesia.
Saya juga sependapat dengan pasangan dengan pasangan nomor urut satu terutama yang disampaikan Gus Muhaimin, sahabat lama saya. Saya juga punya pantun Gus Muhaimin
Satu dua cempaka biru
Tiga empat dalam jabangan
Kalau mendapat kawan baru
Kawan lama dilupa jangan
Saya sependapat dan saya bersyukur, dan saya gembira suasana hari ini, suasana penuh kekeluargaan, penuh riang gembira, penuh dengan saling mengasihi, saling mendukung. Jadi siapapun yang menang kita harus bersatu menjaga negara ini
Wassalamualaikum Warahmatullahi Wabarakatuh"""  #Pidato paslon kedua
text3 = """Assalamualaikum Warahmatullahi Wabarakatuh

Selamat malam, salam sejahtera untuk kita semuanya, Shalom, Om swastiastu, Namo buddhaya, rahayu, salam Pancasila, merdeka.
Yang saya hormati seluruh anggota KPU, Bawaslu, DKPP, terima kasih sudah memberikan sebuah proses kelancaran sampai nomor urut dari masing-masing pasangan sudah ditentukan, dan tentu hadir di sini para pimpinan politi, dari seluruh partai yang saya hormati. Kami senang, riang gembira suasana ini ditunjukkan di depan publik, dan kami ingin itu juga ada dalam hati kita masing-masing.
Saya sangat menghormati situasi ini, tapi izinkan tanpa mengurangi rasa hormat saya untuk menyapa partai pengusung saya. Dari PDIP Ibu Megawati terima kasih, Pak Mardiono dari PPP terima kasih, Pak Hari Tanoe terima kasih dari Perindo, dan Pak OSO dari Hanura, para relawan yang semua hadir, dan seluruh masyarakat Indonesia.
Jadi kita mendapatkan nomor 3 itu pas, sesuai dengan sila ke-3 persatuan Indonesia, kita satukan semuanya dalam proses politik yang menggembirakan. Bapak ibu yang sangat saya hormati, itu lah kegembiraan yang seharusnya kita dapatkan, tapi beberapa hari ini kita sedang disuguhkan untuk menonton drakor yang sangat menarik, publik, pendukung Ganjar-Mahfud saya harap tenang, saya menghormati yang lain, drama-drama itu lah yang sebenarnya tidak perlu terjadi. Dan malam ini memang seharusnya kita sebetulnya sedang memulai, memulai sesuatu perayaan demokrasi melalui Pemilu, dan namun melihat situasi belakangan ini tentu kami mendengarkan banyak pihak. Kita menangkap apa yang menjadi kegelisahan, suasana kebatinan yang muncul di masyarakat. Ada tokoh agama, ada guru-guru bangsa, ada seniman, ada budayawan, ada temen-temen jurnalis, ada para pemred, para aktivis mahasiswa, dan semuanya sedang menyuarakan kegelisahan itu.
Kewajiban kita bapak ibu untuk menjaga, karena kalau kita merasakan itu rasanya demokrasi harus kita pastikan bahwa demokrasi bisa baik meskipun sekarang belum baik-baik saja, kita harus sampaikan itu. Saya tenang kok, dan kami ini tenang semuanya, karena kami sangat yakin ada rakyat Indonesia bersama kami untuk menjaga demokrasi di negeri ini.
Bapak ibu yang sangat saya hormati, perjalan demokrasi ini memang kadang-kadang lurus, kadang-kadang berliku, seperti aliran air, tetapi percayalah air yang mengalir itu dia akan mengikuti arah batinnya. Dia tidak akan bisa dibendung dengan cara apapun.
Dan kalau bendungan itu dia paksakan, dia akan tetap mencari jalannya. Muara itu lah muara demokrasi yang hari ini kita idam-idamkan, dan tentu saja ini lah, kesepakatan hari ini yang mesti kita jaga bersama.
Bapak ibu saya ingin sampaikan dalam kesempatan yang berbahagia ini, setelah ini kita mesti bisa memastikan bahwa arah reformasi mesti kita tuntaskan, demokrasi yang berjalan jurdil, situasi yang bisa berjalan pada rel, dan kita selenggarakan dengan betul-betul membawa integritas yang jauh, jauh sekali dari unsur KKN, harus kita pastikan. Ini lah amanat reformasi, dan ini lah amanat konstitusi yang sekarang kita pegang, dan tentu kita mesti menyelamatkan seluruh golongan, seluruh kelompok masyarakat, dan bagaimana sejatinya kita menjaga NKRI.
Bapak ibu saudara sekalian, diam itu bukan lah pilihan, dan bicara ungkapkan dan laporkan praktik-praktik tidak baik yang mencederai demokrasi. Saya berterima kasih karena pasangan nomor 1 dan pasangan nomor 2 punya komitmen yang sama, kami sangat senang. Mari kita tunjukkan integritas dan kejujuran itu sampai dengan pikiran, batin, dan perkataan kita.
Bapak ibu sekali lagi kami ulang, karena dalam kontestasi ini buat kami ini bukan persoalan Ganjar, bukan persoalan Mahfud, bukan sekadar persoalan kekuasaan, ini adalah persoalan masa depan Indonesia yang mesti kita jaga bersama. Mohon doa mohon dukungannya, bismillahirrahmanirrahim, insaallah pasangan Ganjar-Mahfud siap untuk melaksanakan itu.
Izinkan saya untuk akhiri dengan pantun, dan jagonya pantun adalah Pak Mahfud, silakan pak."""  #Pidato paslon ketiga

# Analisis Sentimen
sentiment1, score1 = analyze_sentiment(text1)
sentiment2, score2 = analyze_sentiment(text2)
sentiment3, score3 = analyze_sentiment(text3)

# Menampilkan hasil analisis sentimen
print(f"Sentimen Pidato 1: {sentiment1} (Skor: {score1})")
print(f"Sentimen Pidato 2: {sentiment2} (Skor: {score2})")
print(f"Sentimen Pidato 3: {sentiment3} (Skor: {score3})")

# Ringkasan Pidato
summary1 = summarize_text(text1, max_sentences=2)
summary2 = summarize_text(text2, max_sentences=2)
summary3 = summarize_text(text3, max_sentences=2)

# Menampilkan ringkasan
print("\nRingkasan Pidato 1:")
print(summary1)
print("\nRingkasan Pidato 2:")
print(summary2)
print("\nRingkasan Pidato 3:")
print(summary3)

# Kata-kata yang paling sering
most_frequent_words1 = get_most_frequent_words(text1, n=10)
most_frequent_words2 = get_most_frequent_words(text2, n=10)
most_frequent_words3 = get_most_frequent_words(text3, n=10)

# Menampilkan kata yang paling sering
print("\nKata yang sering diucapkan dalam Pidato 1:")
print(most_frequent_words1)
print("\nKata yang sering diucapkan dalam Pidato 2:")
print(most_frequent_words2)
print("\nKata yang sering diucapkan dalam Pidato 3:")
print(most_frequent_words3)