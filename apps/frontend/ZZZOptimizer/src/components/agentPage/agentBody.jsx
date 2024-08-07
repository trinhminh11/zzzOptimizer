import React from "react";
import "./agent.css";
import AgentLocalDatabase from "./agentLocalDatabase";
import AgentDatabase from "./agentDatabase";

function AgentBody() {
  return (
    <div className="row agent-body">
      <div className="col-lg-3">
        <AgentDatabase />
      </div>
      <div className="col-lg-9">
        <AgentLocalDatabase />
      </div>
    </div>
  );
}

export default AgentBody;
