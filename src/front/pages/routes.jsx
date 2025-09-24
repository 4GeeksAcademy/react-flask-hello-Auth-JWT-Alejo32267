import { createBrowserRouter, createRoutesFromElements, Route } from "react-router-dom";
import { Layout } from "./Layout";
import { Home } from "./Home";
import { Login } from "./Login";
import { Signup } from "./Signup";
import { Private } from "./Private";
import { Demo } from "./Demo";
import { Single } from "./Single";


export const router = createBrowserRouter(
    createRoutesFromElements(
        <Route path="/" element={<Layout />} errorElement={<h1>Not found!</h1>}>
            <Route index element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/private" element={<Private />} />
            <Route path="/demo" element={<Demo />} />
            <Route path="/single/:theId" element={<Single />} />
        </Route>
    )
);