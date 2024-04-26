<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/DickyAdi/newsTag-Classifier">
  </a>

<h3 align="center">News Tag Classifier</h3>

  <p align="center">
    This simple app can be used to classify a news tag based on news headline or title
    <br />
    <a href="https://github.com/DickyAdi/newsTag-Classifier"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/DickyAdi/newsTag-Classifier/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/DickyAdi/newsTag-Classifier/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/DickyAdi/newsTag-Classifier/blob/master/demo.jpg)

This application automatically tags news headline or title using naive bayes model with tf-idf vectorizer

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Scikit-learn][Sklearn]][Sklearn-url]
- [![NLTK][NLTK]][NLTK-url]
- [![Streamlit][Streamlit]][Streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get the project running locally, you need to install all the prerequisites. Follow this steps below to install the prerequisites.

### Prerequisites

Here we provide one command to install all the prerequisites

- ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DickyAdi/newsTag-Classifier.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

To run the application, open your terminal in the directory of the cloned repo then run this command below

```sh
streamlit run apps/main.py
```

after a while, there should be your default browser popping out the application, if not you can access manually in this url below

```url
localhost:8051
```

you can navigate to predict menu on the sidebar and follow the instructions written in the pages

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the Apache License Version 2.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Dicky Adi - dickyadi44@gmail.com

Project Link: [https://github.com/DickyAdi/newsTag-Classifier](https://github.com/DickyAdi/newsTag-Classifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/DickyAdi/newsTag-Classifier.svg?style=for-the-badge
[contributors-url]: https://github.com/DickyAdi/newsTag-Classifier/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DickyAdi/newsTag-Classifier.svg?style=for-the-badge
[forks-url]: https://github.com/DickyAdi/newsTag-Classifier/network/members
[stars-shield]: https://img.shields.io/github/stars/DickyAdi/newsTag-Classifier.svg?style=for-the-badge
[stars-url]: https://github.com/DickyAdi/newsTag-Classifier/stargazers
[issues-shield]: https://img.shields.io/github/issues/DickyAdi/newsTag-Classifier.svg?style=for-the-badge
[issues-url]: https://github.com/DickyAdi/newsTag-Classifier/issues
[license-shield]: https://img.shields.io/github/license/DickyAdi/newsTag-Classifier.svg?style=for-the-badge
[license-url]: https://github.com/DickyAdi/newsTag-Classifier/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/DickyAdi
[product-screenshot]: demo.jpg
[Sklearn]: https://img.shields.io/badge/scikitlearn-%23F7931E?style=for-the-badge&logo=scikitlearn&logoColor=FFFFFF
[Sklearn-url]: https://scikit-learn.org/stable/
[NLTK]: https://img.shields.io/badge/NLTK-NLTK?style=for-the-badge
[NLTK-url]: https://www.nltk.org/index.html
[Streamlit]: https://img.shields.io/badge/Streamlit-Streamlit?style=for-the-badge
[Streamlit-url]: https://streamlit.io/
