import axios from "./customize_axios";

//Get all WEngines
function DriveDiscService() {
  return axios.get("/drivediscs");
}

function DriveDiscProperty() {
  return axios.get("/drivediscs/property");
}

export { DriveDiscService, DriveDiscProperty };
