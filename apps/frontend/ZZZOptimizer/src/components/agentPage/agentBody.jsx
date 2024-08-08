import React from "react";
import "./agent.css";
import AgentLocalDatabase from "./agentLocalDatabase";
import AgentDatabase from "./agentDatabase";
import { AgentsService } from "../../services/AgentService";
import { useState, useEffect } from "react";

function AgentBody() {
  // set up list for store agent from api
  const [listAgents, setListAgents] = useState([]);

  // set up localstorage to store infomation
  const [listSelectedAgents, setListSelectedAgents] = useState(() => {
    // Check local storage and initialize list
    const storedAgents = localStorage.getItem("selected agent");
    return storedAgents ? JSON.parse(storedAgents) : [];
  });

  // Set up function to store data from api into the list
  useEffect(() => {
    getAgents();
  }, []);

  const getAgents = async () => {
    let res = await AgentsService();
    if (res) {
      setListAgents(res);
    }
  };

  return (
    <div className="row agent-body">
      <div className="col-lg-3">
        <AgentDatabase
          listAgents={listAgents}
          listSelectedAgents={listSelectedAgents}
          setListSelectedAgents={setListSelectedAgents}
        />
      </div>
      <div className="col-lg-9">
        <AgentLocalDatabase
          listSelectedAgents={listSelectedAgents}
          setListSelectedAgents={setListSelectedAgents}
        />
      </div>
    </div>
  );
}

export default AgentBody;
