from setuptools import setup, find_packages

setup(
    name='vpn-connect',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # لیست وابستگی‌ها در اینجا، اگر وجود دارد
    ],
    entry_points={
        'console_scripts': [
            'vpn-connect=vpn_connect:main',  # فرض می‌کنیم تابع main در vpn_connect.py وجود دارد
        ],
    },
)
