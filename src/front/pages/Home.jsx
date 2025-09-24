import { Link } from "react-router-dom";

export const Home = () => {
    return (

        <div className="container py-5">

            <div className="text-center">

                <h1 className="display-3 fw-bold text-primary mb-4 animate__animated animate__fadeIn">Welcome to JWT Authorization App</h1>

                <p className="lead text-muted mb-5 animate__animated animate__fadeIn animate__delay-1s">
                    Secure your application with JWT Authentication. Build your app with ease.
                </p>

                <div className="footer mt-5 py-3 text-center">
                    <p className="text-muted">
                        Check the <a target="_blank" href="https://4geeks.com/docs/start/react-flask-template" className="text-primary text-decoration-none fw-semibold hover-link">documentation</a> and
                        <a target="_blank" href="https://4geeks.com/interactive-coding-tutorial/jwt-authentication-with-flask-react" className="text-primary text-decoration-none fw-semibold hover-link">requirements</a>
                    </p>
                </div>

            </div>

        </div>

    );
};