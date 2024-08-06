import React from "react";
import AgentLocalDatabase from "./agentLocalDatabase";
import AgentInfo from "../../../../../backend/components/agents/agentInfo";
import "./agent.css";

function agentBody() {
  return (
    <div className="row agent-body">
      <div className="col-lg-3">
        <AgentInfo />
      </div>
      <div className="col-lg-9">
        <AgentLocalDatabase />
      </div>
    </div>
  );
}

export default agentBody;
