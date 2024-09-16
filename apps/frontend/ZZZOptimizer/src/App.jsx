import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/HomePage/Home";
import AgentPage from "./components/agentPage/agentPage";
import WEnginePage from "./components/wEnginePage/WEnginePage";
import DriveDiskPage from "./components/DriveDiskPage/DriveDiskPage";

function App() {
  return (
    <>
      <div>
        <Routes>
          <Route path="/deploy-github/" element={<Home />}></Route>
          <Route path="/deploy-github/agents" element={<AgentPage />}></Route>
          <Route
            path="/deploy-github/w-engine"
            element={<WEnginePage />}
          ></Route>
          <Route
            path="/deploy-github/drive-disk"
            element={<DriveDiskPage />}
          ></Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
