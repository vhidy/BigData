# Instalasi Miniconda
Miniconda adalah versi minimal dari Anaconda, kedua tools ini adalah untuk membuat lingkungan virtual untuk Python, berikut ini adalah cara instalasi Miniconda :
1. Pertama, downloa dulu berkas miniconda di [https://conda.io/miniconda.html](https://conda.io/miniconda.html)
2. Ubah mode agar berkas bisa dieksekusi dengan perintah `chmod +x Miniconda3-latest-Linux-x86_64.sh`
3. Kemudian eksekusi berkas tersebut dengan perintah `./Miniconda3-latest-Linux-x86_64.sh`
4. Ikuti langkah-langkah
    - Jika muncul `Please, press ENTER to continue` tekan **enter**
    - Kemudian tekan enter sampai `Do you accept the license terms? [yes|no]` tulis **yes** kemudian enter
    - Kemudian jika muncul prompt seperti dibawah ini tekan enter saja
    ```
    Miniconda3 will now be installed into this location:
    /home/idiot/miniconda3

    - Press ENTER to confirm the location
    - Press CTRL-C to abort the installation
    - Or specify a different location below

    [/home/idiot/miniconda3] >>>
    ```
    - Jika muncul prompt tulis **yes** kemudian enter
    ```
    Do you wish the installer to prepend the Miniconda3 install location
    to PATH in your /home/idiot/.bashrc ? [yes|no]
    ```
    - Tunggu sampai selesai kemudian miniconda sudah siap digunakan
    - Untuk memastika conda sudah berhasil diinstall jalankan perintah `conda --version` jika muncul versi conda seperti `conda 4.5.11` maka miniconda sudah berhasil diinstal dengan benar

<hr />

# Instalasi Apache Airflow
Apache Airflow adalah salah satu framework ETL (extract,transform, and load) yang populer, Airflow dibuat menggunakan Python dan microframework Flask, ini mendukung banyak utilitas diantaranya: S3, LDAP, Hadoop, Hive dan juga mendukung beberapa koneksi database yaitu Postgres, MySQL, dan Redis, berikut ini adalah cara instalasi Apache Airflow
yang menggunakan Postgres, Redis, dan Sync (Gunicorn sebagai backend worker)
1. Tambahkan PATH Variable dengan perintah `export AIRFLOW_HOME=~/airflow` dan `export SLUGIFY_USES_TEXT_UNIDECODE=yes`
2. Buat direktori untuk Airflow dengan perintah `mkdir $AIRFLOW_HOME`
3. Instal Airflow dengan perintah `pip install apache-airflow[async,postgres,redis]`
4. Kemudian inisialisasi database untuk backend airflow dengan perintah `airflow initdb`
5. Buka website airflow dengan perintah `airflow webserver -p 8080` kemudian kunjungi 
6. Jika instalasi berjalan dengan baik maka tampilan web airflow seperti berikut
![Airflow web](./airflow-web.png)

Pada direktori `AIRFLOW_HOME` terdapat beberapa berkas konfigurasi, DAGs, dan Scheduler, seperti berikut ini :
```
/home/idiot/.airflow
├── airflow.cfg
├── airflow.db
├── logs
│   └── scheduler
│       ├── 2018-11-10
│       ├── 2018-11-15
│       └── latest -> /home/idiot/.airflow/logs/scheduler/2018-11-15
└── unittests.cfg

5 directories, 3 files
```

berkas `airflow.cfg` digunakan untuk menyimpan atau mengatur konfigurasi untuk airflow, anda dapat mengubahnya sesuai selera anda, sepeerti koneksi database, direktori DAGs, log format, timezone, executor, dll.

<hr />

# Apache Airflow Tutorial
Apache Airflow menggunakan pendekatan DAG (Direct Acyclic Graph) untuk mengatur ETL atau Pipeline, berikut ini adalah tutorial sederhana bagaimana cara mendefinisikan berkas DAG yang diambil dari dokumentasi resmi Apache Airflow

## Import Module
Pertama, kita perlu mengimpor modul Airflow dan modul pendukung lain yang akan kita gunakan untuk alur DAG
```python
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
```

## Arguments
Kita akan membuat DAG dan beberapa tugas untuk membuat pipeline, dan kita memiliki pilihan secara eksplisit menyampaikan serangkaian argumen ke setiap konstruktor tugas (_task_) dan kita dapat mendefinisikan parameter berupa dictionary secara default yang dapat kita gunakan saat membuat tugas. Berikut ini contoh kodenya

```python
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
```

> Untuk informasi lebih lanjut tentang parameter `BaseOperator` dan apa yang mereka lakukan dibalik itu, silakan kunjungi dokumentasi tentang [airflow.models.BaseOperator](https://airflow.apache.org/code.html#airflow.models.BaseOperator)

Selain itu, perhatikan bahwa kita dapat dengan mudah menentukan serangkaian argumen yang berbeda yang akan melayani tujuan yang berbeda pula. Contohnya adalah pengaturan yang berbeda untuk lingkungan production dan development bahkan lingkungan testing.

## Inisiasi DAG
Kami membutuhkan objek DAG, objek ini yang sebelumnya kita impor dari modul kelas Airflow untuk menyatukan task. Di sini kita dapat memberikan string yang mendefinisikan `dag_id`, yang berfungsi sebagai _unique identifier_ untuk DAG kita. Kita juga perlu menambahkan argumen yang sebelumnya kita buat dan interval penjadwalan eksekusi DAG yaitu setiap sehari sekali, berikut ini adalah contoh kode untuk instansiasi kelas DAG.

```python
dag = DAG(
    'tutorial', default_args=default_args, schedule_interval=timedelta(1))
```

## Tasks
Tugas dibuat saat instantiasi objek operator. Sebuah objek yang digunakan oleh seorang operator disebut konstruktor. Argumen pertama `task_id` bertindak sebagai _unique identifier_ untuk tugas tersebut. Berikut ini kita mendefinisikan dua tugas yaitu `t1` dan `t2`

```python
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)
```

Aturan yang diutamakan untuk suatu tugas adalah sebagai berikut:
1. Melewati argumen secara eksplisit
2. Nilai-nilai yang ada di dalam dictionary `default_args`
3. Nilai default operator, jika ada

> Sebuah task harus menyertakan atau mewarisi argumen `task_id` dan `owner`, jika tidak, Airflow akan memberikan pengecualian atau error.

## Templating dengan pustaka Jinja2
Airflow memanfaatkan pustaka Jinja untuk templating dan menyediakan penulisan pipeline dengan satu set parameter dan makro yang terintegrasi. Airflow juga menyediakan _hooks_ (pengait) untuk pipeline yang digunakan untuk menentukan parameter, makro, sehingga kita dapat mendefinisikan atau mengaturnya sesuai dengan selera dengan tujuan agar lebih fleksibel. Penggunaan templating dengan Jinja sama dengan penggunaan seperti biasanya yaitu diawali dengan `{{` dan diakhiri dengan `}}`, berikut ini adalah contoh templating jinja yang akan kita gunakan

```python
templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7) }}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)
```

## Mengatur Dependencies
Jadi sejauh ini kita memiliki dua task sederhana yang tidak bergantung satu sama lain. Berikut beberapa cara untuk dapat menentukan ketergantungan di antara task tersebut:

```python
t2.set_upstream(t1)
t3.set_upstream(t1)
```

Perhatikan bahwa ketika menjalankan skrip DAG, Airflow akan error ketika menemukan siklus dalam DAG atau ketika ketergantungan dirujuk lebih dari satu kali.

## Menjalankan DAG
Saatnya menjalankan beberapa percobaan. Simpan kode-kode dari langkah-langah sebelumnya pada berkas dengan nama `tutorial.py` dalam folder DAGs yang direferensikan di `airflow.cfg` yaitu `~/airflow/dags`. Jika belum ada direktori dags didalam folder airflow buatlah terlebih dahulu. Kemudian jalankan perintah berikut untuk mengeksekusi DAG yang sudah kita buat

```bash
python $AIRFLOW_HOME/dags/tutorial.py
```

Jika kode yang kita buat tidak mengalami error dan kita, kurang lebih akan muncul prompt seperti berikut ini:

```
[2018-11-15 11:26:42,757] {settings.py:174} INFO - setting.configure_orm(): Using pool settings. pool_size=5, pool_recycle=1800
```

## Command Line Metadata Validation
Mari jalankan beberapa perintah untuk memvalidasi skrip ini lebih lanjut.

Menampilkan daftar DAG yang sedang aktif
```bash
airflow list_dags
```

Output
```
-------------------------------------------------------------------
DAGS
-------------------------------------------------------------------
example_bash_operator
example_branch_dop_operator_v3
example_branch_operator
example_http_operator
example_kubernetes_executor
example_passing_params_via_test_command
example_python_operator
example_short_circuit_operator
example_skip_dag
example_subdag_operator
example_subdag_operator.section-1
example_subdag_operator.section-2
example_trigger_controller_dag
example_trigger_target_dag
example_xcom
latest_only
latest_only_with_trigger
test_utils
tutorial
```

Menampilkan detail task tutorial 
```bash
airflow list_tasks tutorial
```

Output
```
print_date
sleep
templated
```

Menampilkan hirarki sebuah task untuk DAG tutorial
```bash
airflow list_tasks tutorial --tree
```

Output
```
<Task(BashOperator): sleep>
    <Task(BashOperator): print_date>
<Task(BashOperator): templated>
    <Task(BashOperator): print_date>
```

## Percobaan
Mari kita uji dengan menjalankan contoh tugas pada tanggal tertentu. Tanggal yang ditentukan dalam konteks ini adalah `execution_date`, yang mensimulasikan penjadwalan yang menjalankan task atau dag pada tanggal dan waktu tertentu:

Testing print_date
```bash
# testing print_date
airflow test tutorial print_date 2018-11-15
```

Testing sleep
```bash
airflow test tutorial sleep 2018-11-15
```

> Format perintah: command subcommand dag_id task_id date

Masih ingat apa yang kita lakukan dengan template sebelumnya menggunakan Jinja? Lihat bagaimana template ini dirender dan dijalankan dengan menjalankan perintah ini:

```bash
airflow test tutorial templated 2018-11-15
```

Berikut ini tampilan struktur hirarki DAG tutorial pada web Airflow

![Untitle](./airflow-web1.png)

## Backfill
Rentang tanggal dalam konteks ini adalah `start_date` dan opsional `end_date`, yang digunakan untuk mengisi jadwal eksekuasi dengan instance task dari DAG ini.

Menjalankan backfill menggunakan rentang tanggal
```bash
airflow backfill tutorial -s 2018-11-15 -e 2018-11-20
```
