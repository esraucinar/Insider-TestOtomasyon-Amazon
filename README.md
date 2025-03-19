# Bootcamp Automation Project

This project is an automated test script for **Amazon Turkey (https://www.amazon.com.tr/)** using **Python + Selenium**. It follows the **Page Object Model (POM)** structure to ensure maintainability and scalability.

## 📌 Requirements
- The test case should be written using **any programming language** and framework.
- **Preferred:** **Python + Selenium**
- ❌ **No BDD frameworks** (Cucumber, Quantum, Codeception, etc.)
- ✅ The test should fully meet **POM requirements**.

## ⚙️ Technologies Used
- **Programming Language:** Python 🐍
- **Automation Framework:** Selenium WebDriver 🚀
- **Test Runner:** unittest
- **Page Object Model (POM) Architecture** implemented

## 📋 Test Case Steps
1️⃣ **Go to Amazon Turkey:** Navigate to [Amazon Turkey](https://www.amazon.com.tr/).  
2️⃣ **Verify Home Page:** Ensure that the homepage loads correctly.  
3️⃣ **Search for a Product:** Type `'Samsung'` in the search bar and perform a search.  
4️⃣ **Verify Search Results:** Confirm that Samsung-related results appear on the search page.  
5️⃣ **Navigate to Page 2:** Click on the **2nd page** from the search results and verify that it loads.  
6️⃣ **Select a Product:** Click on the **3rd product** on the page.  
7️⃣ **Verify Product Page:** Ensure that the selected product’s page is displayed.  
8️⃣ **Add to Cart:** Click the **"Add to Cart"** button.  
9️⃣ **Verify Addition:** Confirm that the product was successfully added to the cart.  
🔟 **Go to Cart:** Navigate to the **Cart Page**.  
1️⃣1️⃣ **Verify Cart:** Check that the correct product is in the cart.  
1️⃣2️⃣ **Remove from Cart:** Delete the product from the cart and verify that it was removed.  
1️⃣3️⃣ **Return to Home Page:** Navigate back to the homepage and confirm the page is correct.  



## 🛠 How to Run the Test

### 1️⃣ Clone the repository:
```bash
git clone <repository-url>
2️⃣ Navigate to the project folder:
bash
Kopyala
Düzenle
cd Bootcamp2025-TestOtomasyon
3️⃣ Install dependencies:
bash
Kopyala
Düzenle
pip install -r requirements.txt
4️⃣ Run the test using unittest:
bash
Kopyala
Düzenle
python -m unittest discover -s test
📂 Project Structure
Kopyala
Düzenle
Bootcamp2025-TestOtomasyon
│── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── category_page.py
│   ├── cart_page.py
│── tests/
│   ├── test_amazonwebsite.py
│── screenshots/
│── requirements.txt
│── README.md
📸 Screenshots:
During the test execution, screenshots are captured and saved in the screenshots/ directory.





