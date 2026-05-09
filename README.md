# Hệ Thống Đề Xuất Sản Phẩm Cho Người Tiêu Dùng

## Giới Thiệu

Dự án xây dựng hệ thống đề xuất sản phẩm thông minh dành cho nền tảng thương mại điện tử, giúp cá nhân hóa trải nghiệm mua sắm của người dùng thông qua việc phân tích hành vi và đặc trưng sản phẩm.

Hệ thống sử dụng mô hình **Hybrid Recommendation System** kết hợp giữa:

* Content-Based Filtering
* TF-IDF
* Word2Vec

Dữ liệu được thu thập realtime từ các nền tảng thương mại điện tử thông qua kỹ thuật Web Crawling và xử lý bằng Python.

---

# Mục Tiêu Dự Án

* Xây dựng hệ thống đề xuất sản phẩm cá nhân hóa cho người tiêu dùng.
* Hỗ trợ người dùng tìm kiếm sản phẩm phù hợp nhanh chóng.
* Tối ưu trải nghiệm mua sắm trên nền tảng thương mại điện tử.
* Ứng dụng Machine Learning và NLP vào bài toán Recommendation System.

---

# Chức Năng Chính

## 1. Gợi ý sản phẩm theo từng khách hàng

Hệ thống phân tích lịch sử tương tác và hành vi mua sắm để đưa ra danh sách sản phẩm phù hợp với từng người dùng.

## 2. Truy cập nhanh đến sản phẩm

Mỗi sản phẩm được gắn trực tiếp liên kết truy cập giúp người dùng xem chi tiết sản phẩm nhanh chóng.

## 3. Đề xuất sản phẩm nổi bật cho nhóm khách hàng tương đồng

Ứng dụng cơ chế Hybrid Recommendation để phát hiện các nhóm khách hàng có hành vi tương tự và đề xuất:

* Sản phẩm nổi bật
* Sản phẩm mới
* Sản phẩm xu hướng

---

# Công Nghệ Sử Dụng

## Ngôn ngữ & Framework

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* TensorFlow / Keras
* MLlib

## Web Crawling

* Requests
* BeautifulSoup
* Selenium

## Recommendation Techniques

* Content-Based Filtering
* TF-IDF Vectorization
* Word2Vec Embedding
* Hybrid Recommendation System

---

# Dataset

Dữ liệu được thu thập realtime từ các website thương mại điện tử thông qua hệ thống crawler tự động.

## Dữ liệu bao gồm:

* Tên sản phẩm
* Thương hiệu
* Giá bán
* Giá khuyến mãi
* Đánh giá sản phẩm
* Số lượng review
* Nhà bán hàng
* Khu vực bán
* Link sản phẩm
* Hình ảnh sản phẩm

## Đặc điểm dữ liệu:

* Dữ liệu lớn
* Dữ liệu realtime
* Có xử lý trùng lặp
* Có tiền xử lý và chuẩn hóa dữ liệu

---

# Kiến Trúc Pipeline

```text
Web Crawling
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering
      ↓
TF-IDF / Word2Vec Vectorization
      ↓
Hybrid Recommendation Model
      ↓
Recommendation Engine
      ↓
Streamlit Deployment
```

---

# Kiến Trúc Hệ Thống Đề Xuất

##  Content-Based Filtering

Phân tích:

* Tên sản phẩm
* Mô tả
* Thương hiệu
* Danh mục

để tìm các sản phẩm có độ tương đồng cao.

---

## TF-IDF

Sử dụng kỹ thuật TF-IDF để:

* Vector hóa văn bản
* Trích xuất đặc trưng sản phẩm
* Tính độ tương đồng bằng Cosine Similarity

---

## Word2Vec

Sử dụng Word2Vec để:

* Học semantic embedding
* Biểu diễn ngữ nghĩa sản phẩm
* Cải thiện khả năng recommendation

---

# Kết Quả Dự Án

Hệ thống:

* Xây dựng thành công pipeline recommendation hoàn chỉnh
* Tự động thu thập dữ liệu từ sàn thương mại điện tử
* Hỗ trợ recommendation realtime
* Có giao diện trực quan bằng Streamlit
* Hỗ trợ truy cập trực tiếp đến sản phẩm

Ngoài ra:

* Có khả năng mở rộng cho Big Data
* Có thể tích hợp Deep Learning Recommendation trong tương lai

---

# Giao Diện Ứng Dụng

## Các thành phần chính:

* Dashboard sản phẩm
* Gợi ý theo người dùng
* Hiển thị sản phẩm nổi bật
* Tìm kiếm sản phẩm
* Điều hướng trực tiếp đến link mua hàng

---

# Cấu Trúc Thư Mục

```text
├── data/
│   ├── raw_data
│   ├── processed_data
├── crawler/
│   ├── lazada_crawler.py
├── app/
│   ├── streamlit_app.py
├── run.py
├── requirements.txt
└── README.md
```

---

# Hướng Dẫn Chạy Dự Án

## 1. Clone Repository

```bash
git clone <https://github.com/LuuNhatNamm/NCKH_2026.git>
cd <NCKH>
```

---

## 2. Cài Đặt Thư Viện

```bash
pip install -r requirements.txt
```

---

## 3. Chạy Hệ Thống

```bash
python run.py
```

Hoặc chạy giao diện Streamlit:

```bash
streamlit run app/streamlit_app.py
```

---

# Nội Dung Nghiên Cứu

Dự án được phát triển dựa trên đề tài nghiên cứu khoa học:

> “Xây dựng hệ thống đề xuất lựa chọn sản phẩm cho người tiêu dùng”

Nội dung nghiên cứu bao gồm:

* Thu thập dữ liệu thương mại điện tử
* Tiền xử lý dữ liệu
* Recommendation System
* NLP trong hệ thống gợi ý
* Hybrid Recommendation
* Triển khai hệ thống thực tế

---

# Hướng Phát Triển

* Tích hợp Collaborative Filtering
* Triển khai Deep Learning Recommendation
* Hỗ trợ Recommendation realtime bằng Spark
* Tối ưu hiệu suất cho Big Data
* Tích hợp API recommendation

---

# Thành Viên Thực Hiện

* Lưu Nhật Nam
* Hà Quang Vinh
* Trần Trọng Chinh

### Giảng viên hướng dẫn

* ThS. Trần Chí Lê

---

# License

This project is developed for academic and research purposes.
