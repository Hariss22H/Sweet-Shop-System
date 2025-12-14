import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const registerUser = (data) =>
  API.post("/api/auth/register", data);

export const loginUser = (data) =>
  API.post("/api/auth/login", data);

export default API;

export const getSweets = () =>
  API.get("/api/sweets");

export const purchaseSweet = (id) =>
  API.post(`/api/sweets/${id}/purchase`);
