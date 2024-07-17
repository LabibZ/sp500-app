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

<div align="center">
  <br />
  <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="python" />
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  </div>
  <h3 align="center">Stock Analysis and Visualization Tool</h3>
  <!-- <img src="https://i.imgur.com/WzDeh0T.png" alt="Project Banner"> -->
  </br>
  
  <a href="https://labibz-sp500.streamlit.app/">View Demo</a>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#🤖-about">About</a>
    </li>
    <li><a href="#⚙️-tech-stack">Tech Stack</a></li>
    <li>
      <a href="#🚀-getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## 🤖 About

This tool retrieves the list of the S&P 500 (from Wikipedia) and its corresponding stock closing price (year-to-date) allowing users to analyze and visualize stock prices, providing features like:

- Comparing closing prices for up to 5 companies,
- Grouping by sector
- Filtering by start and end dates
- Moving Averages
- Candlestick charts

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⚙️ Tech Stack

- Python
- pandas
- NumPy
- streamlit
- matplotlib
- seaborn
- plotly
- yfinance

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 🚀 Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- [Python 3.8+](https://www.python.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/LabibZ/sp500-app.git
   ```
2. Install all the necessary Python packages: pandas, NumPy, streamlit, yfinance, matplotlib, seaborn, plotly
   ```sh
   pip install <python_package>
   ```
3. Run streamlit app
   ```sh
   streamlit run sp500-app.py
   ```
   Open [http://localhost:8501](http://localhost:8501) in your browser to view the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
