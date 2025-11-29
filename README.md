# Laptop Price Predictor API

A Flask-based REST API that predicts laptop prices using a machine learning model. This service provides price predictions based on laptop specifications such as RAM, weight, display features, brand, and hardware components.

## 📁 Project Structure

```
website/
├── app.py                 # Main Flask application
├── model/                 # Machine learning models directory
│   ├── predictor.pickle   # Trained prediction model
│   └── model_columns.pkl  # Feature columns for the model
├── env/                   # Python virtual environment
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
```

## 🚀 Features

- RESTful API for laptop price prediction
- Support for multiple laptop brands (Acer, Apple, ASUS, Dell, HP, Lenovo, MSI, Toshiba)
- Hardware specifications input (CPU, GPU, RAM, Storage)
- Display features (Touchscreen, IPS panel)
- Multiple OS support (Windows, macOS, Linux, Chrome OS, Android)
- JSON-based request/response format

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **Pandas** - Data manipulation
- **Pickle** - Model serialization
- **Scikit-learn** - Machine learning (model training)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/binojmadhuranga/prediction-server.git
   cd website
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate

   # Linux/macOS
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask pandas scikit-learn
   ```

## 🎮 Usage

### Starting the Server

```bash
python app.py
```

The server will start on `http://localhost:5001`

### API Endpoints

#### 1. Home Endpoint
```
GET /
```

**Response:**
```json
{
  "service": "Laptop Price Predictor",
  "status": "running"
}
```

#### 2. Price Prediction Endpoint
```
POST /predict
```

**Request Body:**
```json
{
  "company": "dell",
  "typename": "notebook",
  "ram": 8,
  "weight": 2.5,
  "touchscreen": 0,
  "ips": 1,
  "opsys": "windows10",
  "cpu": "intelcorei5",
  "gpu": "intel"
}
```

**Request Parameters:**

| Parameter | Type | Description | Possible Values |
|-----------|------|-------------|-----------------|
| `company` | string | Laptop manufacturer | acer, apple, asus, dell, hp, lenovo, msi, other, toshiba |
| `typename` | string | Laptop type | 2in1convertible, gaming, netbook, notebook, ultrabook, workstation |
| `ram` | integer | RAM in GB | Any positive integer |
| `weight` | float | Weight in kg | Any positive float |
| `touchscreen` | integer | Touchscreen support | 0 (No) or 1 (Yes) |
| `ips` | integer | IPS display | 0 (No) or 1 (Yes) |
| `opsys` | string | Operating system | android, chromeos, linux, macosx, noos, windows10, windows10s, windows7, macos |
| `cpu` | string | CPU type | amd, intelcorei3, intelcorei5, intelcorei7, other |
| `gpu` | string | GPU type | amd, intel, nvidia |

**Success Response:**
```json
{
  "success": true,
  "prediction": 45000.50
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message description"
}
```

## 📝 Example Usage

### Using cURL
```bash
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{
    "company": "apple",
    "typename": "ultrabook",
    "ram": 16,
    "weight": 1.5,
    "touchscreen": 0,
    "ips": 1,
    "opsys": "macosx",
    "cpu": "intelcorei7",
    "gpu": "intel"
  }'
```

### Using Python
```python
import requests

url = "http://localhost:5001/predict"
data = {
    "company": "dell",
    "typename": "gaming",
    "ram": 16,
    "weight": 2.8,
    "touchscreen": 0,
    "ips": 1,
    "opsys": "windows10",
    "cpu": "intelcorei7",
    "gpu": "nvidia"
}

response = requests.post(url, json=data)
print(response.json())
```

### Using JavaScript (Fetch API)
```javascript
fetch('http://localhost:5001/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    company: 'hp',
    typename: 'notebook',
    ram: 8,
    weight: 2.0,
    touchscreen: 1,
    ips: 1,
    opsys: 'windows10',
    cpu: 'intelcorei5',
    gpu: 'intel'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🔧 Model Information

The prediction model uses:
- **Numeric Features**: RAM, Weight, Touchscreen, IPS
- **Categorical Features**: Company, Type, OS, CPU, GPU (one-hot encoded)
- Pre-trained model stored in `model/predictor.pickle`
- Feature columns stored in `model/model_columns.pkl`

## 📦 Dependencies

```
Flask>=2.0.0
pandas>=1.3.0
scikit-learn>=0.24.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Binoj Madhuranga**
- GitHub: [@binojmadhuranga](https://github.com/binojmadhuranga)

## 🐛 Issues

If you encounter any issues or have suggestions, please file an issue on the [GitHub repository](https://github.com/binojmadhuranga/prediction-server/issues).

## 📞 Support

For support, email or open an issue in the repository.

---

**Note**: Make sure the model files (`predictor.pickle` and `model_columns.pkl`) are present in the `model/` directory before running the application.
