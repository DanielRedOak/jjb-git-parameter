from setuptools import setup

setup(
    name='jjb-git-parameter',
    version='0.1',
    description='Jenkins Job Builder Git Parameter',
    url='https://github.com/danielredoak/jjb-git-parameter',
    author="Ryan O'Keeffe",
    author_email='okeefferd@gmail.com',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.parameters': [
            'git = jjb_git_parameter.git:git_parameter']
    },
    packages=['jjb_git_parameter'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
