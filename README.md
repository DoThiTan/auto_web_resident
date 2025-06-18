# Auto Test Web với Pytest + Playwright + Python
## Cài môi trường
- Cài python
- Cài pytest
  pip install pytest
- Cài playwright cho python:
  pip install playwright
  playwright install
- Cài allure để có HTML report
  pip install allure-pytest
- Có thể chạy luôn lệnh trên để cài playwright, pytest, allure-pytest  : pip install -r requirements.txt 
- Tạo virtual environment
  python -m venv venv
  source venv/bin/activate  // Trên Linux/macOS
  venv\Scripts\activate     // Trên Windows
## Lệnh chạy
- Chạy all test với trình duyệt:
  pytest --browser_name=firefox
  pytest --browser_name=chromium
- Chạy từng file:
  pytest path/to/test_file.py
- Xuất báo cáo:
  pytest --alluredir=reports
  allure serve reports
