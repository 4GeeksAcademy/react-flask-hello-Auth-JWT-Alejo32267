
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export const Signup = () => {
    const [form, setForm] = useState({ email: "", password: "" });
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        try {
            const res = await fetch(import.meta.env.VITE_BACKEND_URL + "/api/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                credentials: "include",
                body: JSON.stringify(form)
            });

            const data = await res.json();

            if (res.ok) {
                alert("Signup successful! You may now log in.");
                navigate("/login");
            } else {
                setError(data.msg || "Sign up failed.");
            }
        } catch (error) {
            console.error("Sign up error:", error);
            setError("A network error occurred.");
        }
    };

    return (
        <div className="container mt-5" style={{ maxWidth: "400px" }}>
            <h2 className="mb-4 text-center text-primary">Sign Up</h2>

            {error && <div className="alert alert-danger text-center p-3 rounded-3 shadow-sm">{error}</div>}

            <form onSubmit={handleSubmit} className="shadow-lg p-4 rounded-4 bg-white">
                <div className="mb-3">
                    <input
                        type="email"
                        className="form-control rounded-3 border-2 p-3"
                        placeholder="Email"
                        required
                        value={form.email}
                        onChange={e => setForm({ ...form, email: e.target.value })}
                    />
                </div>
                <div className="mb-4">
                    <input
                        type="password"
                        className="form-control rounded-3 border-2 p-3"
                        placeholder="Password"
                        required
                        value={form.password}
                        onChange={e => setForm({ ...form, password: e.target.value })}
                    />
                </div>
                <button type="submit" className="btn btn-success w-100 py-2 rounded-3 text-white fw-semibold shadow-sm transition-all hover-bg-success">
                    Sign Up
                </button>
            </form>
        </div>

    );
};