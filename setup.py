from setuptools import setup, find_packages
import re
import io

with open('README.md', 'r') as f:
    long_description = f.read()

with io.open('fake_exmoslem_questions/__version__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='Fake-exMoslem-Questioner',
    version=version,
    author='AbdullahM0hamed',
    description='Generate fake islamic questions to catxh out fake ex-muslims. Inspired by "how many rakat in sura fatihah"',
    packages=find_packages(),
    url='https://github.com/AbdullahM0hamed/Fake-exMoslem-Questions',
    install_requires=[
        'requests>=2.18.4',
        'beautifulsoup4>=4.6.0'
    ],

    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        fake-question=fake_exmoslem_questions.question_generator:main
    '''
)
