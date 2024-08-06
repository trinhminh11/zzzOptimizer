import NavCategories from "./NavCategories";
import NavLogo from "./NavLogo";
import "./nav.css";

export default function NavBar() {
  return (
    <nav className="header-nav ms-auto">
      <ul className="d-flex align-items-center nav-ul">
        <NavLogo />
        <NavCategories />
      </ul>
    </nav>
  );
}
