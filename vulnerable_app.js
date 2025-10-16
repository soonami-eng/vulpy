// Vulnerable JavaScript Application for Security Testing
// This file contains intentional security vulnerabilities for testing purposes

const express = require('express');
const app = express();

// VULNERABILITY 1: Hardcoded credentials
const DATABASE_PASSWORD = 'SuperSecret123!';
const API_KEY = 'sk-1234567890abcdef';
const AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY';

// VULNERABILITY 2: SQL Injection
app.get('/user', (req, res) => {
    const userId = req.query.id;
    const query = "SELECT * FROM users WHERE id = '" + userId + "'";
    // Direct string concatenation allows SQL injection
    database.query(query);
});

// VULNERABILITY 3: Command Injection
app.get('/ping', (req, res) => {
    const host = req.query.host;
    const cmd = 'ping -c 4 ' + host;
    exec(cmd, (error, stdout, stderr) => {
        res.send(stdout);
    });
});

// VULNERABILITY 4: eval() usage with user input
app.post('/calculate', (req, res) => {
    const expression = req.body.expr;
    const result = eval(expression); // Dangerous!
    res.json({ result: result });
});

// VULNERABILITY 5: Cross-Site Scripting (XSS)
app.get('/search', (req, res) => {
    const searchTerm = req.query.q;
    res.send('<h1>Search results for: ' + searchTerm + '</h1>');
});

// VULNERABILITY 6: Insecure deserialization
app.post('/deserialize', (req, res) => {
    const userInput = req.body.data;
    const obj = JSON.parse(userInput);
    eval(obj.code); // Double vulnerability!
});

// VULNERABILITY 7: Path traversal
app.get('/download', (req, res) => {
    const filename = req.query.file;
    res.sendFile('/var/www/files/' + filename);
});

// VULNERABILITY 8: Insecure random number generation
function generateToken() {
    return Math.random().toString(36).substring(7);
}

// VULNERABILITY 9: Missing authentication
app.delete('/user/:id', (req, res) => {
    const userId = req.params.id;
    database.deleteUser(userId); // No auth check!
    res.send('User deleted');
});

// VULNERABILITY 10: Weak cryptography
const crypto = require('crypto');
function encryptPassword(password) {
    const cipher = crypto.createCipher('des', 'weak-key');
    return cipher.update(password, 'utf8', 'hex') + cipher.final('hex');
}

app.listen(3000, () => {
    console.log('Vulnerable app listening on port 3000');
});
