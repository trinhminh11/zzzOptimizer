import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/HomePage/Home";
import AgentPage from "./components/agentPage/agentPage";

function App() {
  return (
    <>
      <div>
        <Routes>
          <Route path="/deploy-github/" element={<Home />}></Route>
          <Route
            path="/deploy-github/agents"
            element={<AgentPage />}
          ></Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
