import React from "react";
import AgentLocalDatabase from "./agentLocalDatabase";
import AgentProcessing from "../../../../../backend/components/agentProcessing";
import "./agent.css";

function agentBody() {
  return (
    <div className="row agent-body">
      <div className="col-lg-3">
        <AgentProcessing />
      </div>
      <div className="col-lg-9">
        <AgentLocalDatabase />
      </div>
    </div>
  );
}

export default agentBody;
