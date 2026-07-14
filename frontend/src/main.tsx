import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
// @ts-ignore: Fontsource has no type declarations for side-effect import
import "@fontsource/inter";
import Providers from "./app/providers";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Providers>
      <App />
    </Providers>
  </React.StrictMode>,
);
