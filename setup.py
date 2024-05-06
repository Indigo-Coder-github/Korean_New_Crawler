import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setuptools.setup(
    name="korean_news_crawler",
    version="1.0.5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Python Library for Crawling Top 10 Korean News and Providing Synonym Dictionary",
    author="Indigo-Coder",
    author_email="hjs40111@gmail.com",
    url="https://github.com/Indigo-Coder-github/Korean_News_Crawler",
    install_requires=[
        "BeautifulSoup4",
        "selenium"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/Indigo-Coder-github/Korean_News_Crawler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)