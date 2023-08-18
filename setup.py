from setuptools import find_packages, setup

setup(
    name='Lyrics-Scraping',
    version='0.2.0',
    description="Crawler programmed to crawl the website, parse, and scrape relevant lyrics of a particular artist.",
    package_dir={"": "lyrics_crawler"},
    packages=find_packages(where="lyrics_crawler"),
    author='Shahriar Rahman',
    license='MIT',
    author_email='shahriarrahman1101@gmail.com',
    python_requires='>=3.11, <4',
    extras_requires={
        "dev": ["pytest>=7.0", "twine>=4.0.2"]
    },
    install_requires=[
        'setuptools~=68.1.0',
        'scrapy~=2.10.0',
        'scrapy-user-agents~=0.1.1',
    ],

)
