const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const app = express();
app.use(bodyParser.json());

let users = [];

// Register Endpoint
app.post('/user/register', (req, res) => {
    const { email, password, name, lastName, dob } = req.body;

    // 1. Email kontrolü
    const existingUser = users.find(user => user.email === email);
    if (existingUser) {
        return res.status(400).json({ 
            status: false, 
            errorMessage: "Email kayıtlıdır." 
        });
    }

    // 2. Password kontrolü
    if (password.length < 3 || password.length > 12) {
        return res.status(400).json({ 
            status: false, 
            errorMessage: "Password min 3 max 12 karakter olmalıdır." 
        });
    }

    // 3. Yeni kullanıcı oluştur
    const newUser = {
        id: users.length + 1,
        email,
        password,
        name,
        lastName,
        dob
    };

    users.push(newUser);

    res.status(201).json({ 
        status: true, 
        errorMessage: "" 
    });
});

// Login Endpoint
app.post('/user/login', (req, res) => {
    const { email, password } = req.body;

    // Kullanıcıyı bul
    const user = users.find(user => user.email === email && user.password === password);

    if (!user) {
        return res.status(401).json({ 
            status: false, 
            errorMessage: "Email veya password hatalı." 
        });
    }

    // JWT Token oluştur
    const token = jwt.sign({ id: user.id, email: user.email }, 'gizli_anahtar', { expiresIn: '1h' });

    res.status(200).json({ 
        status: true, 
        token 
    });
});

// Me Endpoint
app.get('/user/me', (req, res) => {
    const token = req.headers['authorization'];

    if (!token) {
        return res.status(401).json({ 
            status: false, 
            errorMessage: "Token bulunamadı." 
        });
    }

    // Token'ı doğrula
    jwt.verify(token.split(' ')[1], 'gizli_anahtar', (err, decoded) => {
        if (err) {
            return res.status(401).json({ 
                status: false, 
                errorMessage: "Geçersiz token." 
            });
        }

        // Kullanıcıyı bul
        const user = users.find(user => user.id === decoded.id);

        if (!user) {
            return res.status(404).json({ 
                status: false, 
                errorMessage: "Kullanıcı bulunamadı." 
            });
        }

        // Kullanıcı bilgilerini dön
        res.status(200).json({
            id: user.id,
            email: user.email,
            name: user.name,
            lastName: user.lastName,
            dob: user.dob
        });
    });
});

// Sunucuyu başlat
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
