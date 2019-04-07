import pytest

if __name__ == '__main__':
    pytest.main(['-s','-m=login','--alluredir','./report/xml'])