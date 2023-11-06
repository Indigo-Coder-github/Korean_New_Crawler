import setuptools

setuptools.setup(
    name="korean_news_crawler",
    version="0.0.1",
    author="Indigo-Coder",
    author_email="hjs40111@gmail.com",
    description="Python Library for Crawling Top 10 Korean News and Providing Synonym Dictionary",
    long_description_content_type="text/markdown",
    url="https://github.com/Indigo-Coder-github/Korean_News_Crawler",
    project_urls={
        "Bug Tracker": "https://github.com/Indigo-Coder-github/Korean_News_Crawler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)