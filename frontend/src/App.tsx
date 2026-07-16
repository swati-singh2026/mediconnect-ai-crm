import { BrowserRouter, Routes, Route } from "react-router-dom";

import HCPInteraction from "./pages/HCPInteraction";
import Dashboard from "./pages/Dashboard";
import LogInteraction from "./pages/LogInteraction";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HCPInteraction />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/log-interaction" element={<LogInteraction />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
