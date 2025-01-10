# Final Submission: Student Stress Level Prediction
Nama: Aini Nurpadilah
Username dicoding:Aininrp

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [student lifestyle dataset](https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset/data/) |
| Masalah | Banyak siswa mengalami stres akibat gaya hidup yang tidak seimbang, seperti kurangnya waktu tidur, tekanan akademik, dan minimnya aktivitas fisik. Namun, sulit bagi institusi pendidikan atau konselor untuk memantau tingkat stres siswa secara efektif dan memberikan intervensi yang tepat waktu.|
| Solusi machine learning | Membuat model machine learning yang dapat memprediksi level stres siswa berdasarkan dataset yang mencakup faktor-faktor seperti jam belajar, jam tidur, aktivitas ekstrakurikuler, pola sosial, kebiasaan fisik, dan pencapaian akademik. |
| Metode pengolahan | Data diproses melalui beberapa tahap menggunakan komponen-komponen TFX. Tahapan pemrosesan dimulai dengan pembacaan data dari direktori yang ditentukan melalui CsvExampleGen, yang membagi data menjadi dua bagian, yaitu pelatihan dan evaluasi. Statistik data kemudian dihasilkan oleh StatisticsGen, sementara skema data ditentukan oleh SchemaGen. ExampleValidator memastikan bahwa data tersebut sesuai dengan skema yang ditentukan.  |
| Arsitektur model | Deskripsi arsitektur model yang diguanakan |
| Metrik evaluasi | Metrik yang digunakan dalam proyek prediksi gagal jantung meliputi akurasi, presisi, recall, dan F1-score untuk mengukur kinerja model. Akurasi menunjukkan proporsi prediksi benar, sedangkan presisi, recall, dan F1-score memberikan gambaran tentang keseimbangan antara prediksi benar positif dan negatif. |
| Performa model | Performa model prediksi gagal jantung dinilai menggunakan metrik akurasi, presisi, recall, dan F1-score. Hasil evaluasi menunjukkan bahwa model ini memiliki tingkat akurasi yang tinggi, dengan presisi dan recall yang seimbang, menunjukkan kemampuannya untuk predksi level stres secara efektif dan mengurangi jumlah kesalahan prediksi. |
| Opsi deployment | Proyek machine learning ini dideploy menggunakan salah satu platform as a service yaitu RAILWAY yang menyediakan layanan gratis untuk mendeploy sebuah proyek. |
| Web app |[Student Stress Level Prediction](https://level-stress-prediction.up.railway.app/v1/models/level-stress-prediction/metadata)|
| Monitoring | Monitoring pada proyek ini dapat dilakukan dengan menggunakan layanan open-source yaitu Prometheus. Contohnya setiap perubahan jumlah request yang dilakukan kepada sistem ini dapat dimonitoring dengan baik dan dapat menampilkan status dari setiap request yang diterima.|
