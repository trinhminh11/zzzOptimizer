import React from "react";
import AgentInfo from "../../../../../backend/components/agents/AgentInfo";
import "./agent.css";
import AgentLocalDatabase from "./agentLocalDatabase";

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
