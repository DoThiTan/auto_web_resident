import pytest
from pages.login_page import LoginPage

@pytest.mark.dependency()
def test_login_success_no_remember(page, base_url, context):
    # Test đăng nhập lần đầu
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login_as("admin-01", "Hieu1995@123", remember=False)
    page.wait_for_selector("text=Admin Panel")
    assert page.is_visible("text=Admin Panel"), "Đăng nhập không thành công"
    page.close()
    #Mở context mới (giống như mở cửa sổ trình duyệt mới)
    new_page = context.new_page()
    login_page = LoginPage(new_page, base_url)
    login_page.goto()
    new_page.wait_for_selector("text=Đăng nhập")
    assert new_page.is_visible("text=Đăng nhập"), "Sai mode ghi nhớ đăng nhập"

@pytest.mark.dependency(depends=["test_login_success_no_remember"])
def test_login_success_remember(page, base_url, context):
    #Test đăng nhập lần đầu với remember
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login_as("admin-01", "Hieu1995@123", remember=True)
    page.wait_for_selector("text=Admin Panel")
    assert page.is_visible("text=Admin Panel"), "Đăng nhập không thành công"
    page.close()
    # Mở context mới để kiểm tra remember
    new_page = context.new_page()
    login_page = LoginPage(new_page, base_url)
    login_page.goto()
    new_page.wait_for_selector("text=Admin Panel")
    assert new_page.is_visible("text=Admin Panel"), "Lưu đăng nhập không thành công"
    login_page.logout()

@pytest.mark.dependency(depends=["test_login_success_remember"])
def test_login_success_enter(page, base_url):
    # Test đăng nhập lần đầu
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login_enter_as("admin-01", "Hieu1995@123", remember=False)
    page.wait_for_selector("text=Admin Panel")
    assert page.is_visible("text=Admin Panel"), "Đăng nhập không thành công"

@pytest.mark.dependency(depends=["test_login_success_enter"])
def test_login_failed_username_invalid(page, base_url):
    #Test đăng nhập thất bại với username không tồn tại
    login_page = LoginPage(page, base_url)
    login_page.goto()
    login_page.login_as("admin", "Hieu1995@123")
    page.wait_for_selector("text=Không tìm thấy:")
    assert page.is_visible("text=Không tìm thấy:")
    #Test đăng nhập thất bại với password không đúng
    login_page.delete_textbox()
    login_page.login_as("admin-01", "Hieu1995")
    page.wait_for_selector("text=Yêu cầu không hợp lệ:")
    assert page.is_visible("text=Yêu cầu không hợp lệ:")
    #Test đăng nhập thất bại khi không nhập username
    login_page.delete_textbox()
    login_page.login_as_invalid("", "Hieu1995@123")
    page.wait_for_selector("text=String must contain at least 1 character(s)")
    assert page.is_visible("text=String must contain at least 1 character(s)")
    #Test đăng nhập thất bại khi không nhập password
    login_page.delete_textbox()
    login_page.login_as_invalid("admin-01", "")
    page.wait_for_selector("text=String must contain at least 1 character(s)")
    assert page.is_visible("text=String must contain at least 1 character(s)")
