# 📊 **IMDB-Insights**  
![Waketime](https://img.shields.io/badge/Waketime-21%20hrs%2027%20mins-blueviolet?style=flat&labelColor=black&logo=clock&logoColor=white)

IMDb-Insights is a Python-based project designed to scrape IMDb's **Top 250 TV Shows**, analyze their data, and provide insightful visualizations 📈. This project allows users to explore TV shows by `genres`, `ratings`, and `number of episodes`, while generating stunning visualizations like `bar graphs`, `line graphs`, and `word clouds`.  

✨ _This project was developed as part of the `Introduction to Software Systems` course at **IIIT Hyderabad**._  

---

## 📌 **Features**  
- 🛠 **Data Scraping**: Fetch data from IMDb's Top 250 TV shows using `BeautifulSoup` and store it in a `MySQL database`.  
- 📊 **Data Analysis**: Analyze shows based on `genres`, `IMDb ratings`, and `episode counts`.  
- 🎨 **Visualizations**:  
  - 📈 `Bar Chart`: Genre vs. Number of Shows.  
  - 📉 `Line Graph`: Episode Count vs. Frequency.  
  - ☁️ `Word Cloud`: Highlight filtered TV shows by importance.  
- 🔍 **Interactive Filtering**:  
  - Filter shows by `genre`, `IMDb rating range`, and `episode count range`.  
  - Automatically sort results by `rating` in descending order.  

---

## 🚀 **Installation**  

### 🛠 Prerequisites  
Ensure you have the following installed:  
1. 🐍 `Python 3.7+`  
2. 🛢 **MySQL Server**  
3. 📦 Required Python Libraries:  
   ```bash
   pip install mysql-connector-python beautifulsoup4 matplotlib wordcloud pillow numpy
   ```  

### 🗄 **Database Setup**  
1. Create a `MySQL database` named **`top_250_shows`**.  
2. Grant database access to the user defined in the scripts.  

---

## 🛠️ **Usage**  

### 1️⃣ **Data Scraping and Storage**  
Run the script to scrape IMDb's Top 250 TV shows and store them in the database:  
```bash
python q3_a.py
```  

### 2️⃣ **Interactive Filtering**  
Filter TV shows by custom criteria (genres, ratings, episodes):  
```bash
python q3_b.py
```  

### 3️⃣ **Word Cloud Generation**  
Generate a stunning word cloud for filtered TV shows:  
```bash
python q3_bonus.py
```  

---

## 📊 **Visualizations**  

1. 📊 **Bar Chart**: Displays the `number of TV shows` per genre.  
2. 📈 **Line Graph**: Shows `frequency counts of TV shows` based on episode count.  
3. ☁️ **Word Cloud**: Highlights filtered TV shows with font size based on importance.  

---

## 📂 **Project Structure**  

```plaintext
IMDB-Insights/
├── q3_a.py         # Scrapes data and stores it in the MySQL database
├── q3_b.py         # Filters TV shows based on user input
├── q3_bonus.py         # Generates a word cloud for filtered TV shows
├── index.html      # Contains scraped HTML for reference
├── mask.png        # Word cloud mask image
└── README.md       # Project documentation
```  

---

## ✨ **Future Enhancements**  
- 🎥 Add support for `movies` or other IMDb charts.  
- 📊 Include `dynamic visualizations` using frameworks like Plotly.  
- 🌐 Deploy the project as a `web application`.  

---

## 🧑‍💻 **Author**  
- **Shreyas Mehta** ✍️  
