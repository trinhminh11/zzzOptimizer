import NavAvatar from "./NavAvatar";
import NavCategories from "./NavCategories";
import NavLogo from "./NavLogo";

export default function NavBar() {
  return (
    <nav className="header-nav ms-auto">
      <ul className="d-flex align-items-center">
        <NavLogo />
        <NavCategories />
        <NavAvatar />
      </ul>
    </nav>
  );
}
