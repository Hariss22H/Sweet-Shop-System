import { useEffect, useState } from "react";
import {
  registerUser,
  loginUser,
  getSweets,
  purchaseSweet
} from "./api";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [token, setToken] = useState("");
  const [sweets, setSweets] = useState([]);

  const fetchSweets = async () => {
    const res = await getSweets();
    setSweets(res.data);
  };

  useEffect(() => {
    fetchSweets();
  }, []);

  const handleRegister = async () => {
    try {
      await registerUser({ username, password });
      setMessage("User registered successfully");
    } catch {
      setMessage("Registration failed");
    }
  };

  const handleLogin = async () => {
    try {
      const res = await loginUser({ username, password });
      setToken(res.data.access_token);
      setMessage("Login successful");
    } catch {
      setMessage("Login failed");
    }
  };

  const handlePurchase = async (id) => {
    await purchaseSweet(id);
    fetchSweets();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Sweet Shop Management System</h1>

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <br /><br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br /><br />

      <button onClick={handleRegister}>Register</button>
      <button onClick={handleLogin} style={{ marginLeft: "10px" }}>
        Login
      </button>

      <p>{message}</p>

      <hr />

      <h2>Available Sweets</h2>

      {sweets.map((sweet) => (
        <div key={sweet.id} style={{ marginBottom: "10px" }}>
          <strong>{sweet.name}</strong> ({sweet.category}) - ₹{sweet.price} <br />
          Stock: {sweet.quantity} <br />

          <button
            onClick={() => handlePurchase(sweet.id)}
            disabled={sweet.quantity === 0}
          >
            Purchase
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;
