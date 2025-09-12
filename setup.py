import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    longDescription = f.read()

__vesion__ = "0.0.0"

repoName = "TextSummarizer"
authorUserName = "basajjabaka"
authorEmail = "19basajjabaka@gmail.com"
srcRepo = "TextSummarizer"


setuptools.setup(
    name=repoName,
    version=__vesion__,
    author=authorUserName,
    author_email=authorEmail,
    description="Text Summarization by Basajja",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{authorUserName}/{repoName}",
    project_urls={
        "Bug Tracker": f"https://github.com/{authorUserName}/{repoName}/issues",
    }
        
)