export default function Footer() {
  return (
    <footer className="py-10 px-6" style={{ backgroundColor: "#1B2A4A" }}>
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="text-xl font-bold text-white">
          Tri<span style={{ color: "#4B8FE2" }}>agent</span>
        </div>
        <div className="flex gap-8">
          <a href="#services"    className="text-sm text-gray-400 hover:text-white transition-colors">Services</a>
          <a href="#demo-chat"   className="text-sm text-gray-400 hover:text-white transition-colors">Demo</a>
          <a href="#contact"     className="text-sm text-gray-400 hover:text-white transition-colors">Contact</a>
          <a href="mailto:hello@triagent.cloud" className="text-sm text-gray-400 hover:text-white transition-colors">hello@triagent.cloud</a>
        </div>
        <div className="text-xs text-gray-500">
          &copy; 2026 Triagent. All rights reserved.
        </div>
      </div>
    </footer>
  );
}
