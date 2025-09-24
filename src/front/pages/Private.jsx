import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export const Private = () => {
    const [msg, setMsg] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {

        const fetchPrivateData = async () => {
            const token = sessionStorage.getItem("token");

            if (!token) {
                navigate("/login");
                return;
            }

            try {
                const res = await fetch(
                    import.meta.env.VITE_BACKEND_URL + "/api/private",
                    {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                            Authorization: `Bearer ${token}`
                        }
                    }
                );

                if (!res.ok) {
                    throw new Error("Unauthorized");
                }

                const data = await res.json();
                setMsg(data.msg || "Welcome!");
            } catch (err) {
                console.error("Access denied:", err);
                navigate("/login");
            } finally {
                setLoading(false);
            }
        };

        fetchPrivateData();
    }, [navigate]);

    return (
        <div className="container text-center mt-5">
            {loading ? (
                <div className="d-flex justify-content-center align-items-center">
                    <div className="spinner-border text-primary" role="status" style={{ width: '3rem', height: '3rem' }}>
                        <span className="visually-hidden">Loading...</span>
                    </div>
                    <p className="ms-3 text-muted fs-4">Loading...</p>
                </div>
            ) : (
                <div className="alert alert-info p-4 rounded-3 shadow-lg">
                    <h1 className="text-dark">{msg}</h1>
                </div>
            )}
        </div>

    );
};