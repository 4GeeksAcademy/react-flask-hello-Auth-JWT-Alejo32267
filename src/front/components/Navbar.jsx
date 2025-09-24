import { Link, useNavigate } from "react-router-dom";

export const Navbar = () => {
    const navigate = useNavigate();

    const token = sessionStorage.getItem("token");

    const handleLogout = () => {
        sessionStorage.removeItem("token");
        navigate("/login");
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light shadow-sm rounded-3">

            <div className="container">

                <Link className="navbar-brand fs-4 fw-normal text-primary" to="/">JWT Auth App</Link>

                <div className="ms-auto d-flex gap-3">
                    {!token ? (
                        <>
                            <Link to="/login" className="btn btn-outline-primary px-4 py-2 fs-6 fw-normal border-2 transition-all hover-border" style={{ borderColor: '#007bff' }}>Log In</Link>
                            <Link to="/signup" className="btn btn-success px-4 py-2 fs-6 fw-normal border-0 transition-all hover-shadow-soft">Sign Up</Link>
                        </>
                    ) : (
                        <>
                            <Link to="/private" className="btn btn-outline-primary px-4 py-2 fs-6 fw-normal border-0 transition-all hover-shadow-soft">Private</Link>
                            <button onClick={handleLogout} className="btn btn-danger px-4 py-2 fs-6 fw-normal border-0 transition-all hover-shadow-soft">Log Out</button>
                        </>
                    )}
                </div>
            </div>

        </nav>

    );
};