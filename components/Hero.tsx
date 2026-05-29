export default function Hero() {
  return (
    <section
      className="pt-32 pb-24 px-6"
      style={{ background: "linear-gradient(135deg, #1B2A4A 0%, #2E5FA3 100%)" }}
    >
      <div className="max-w-4xl mx-auto text-center">
        <div
          className="inline-block px-4 py-1.5 rounded-full text-xs font-semibold mb-6 tracking-wide uppercase"
          style={{ backgroundColor: "rgba(75,143,226,0.2)", color: "#4B8FE2" }}
        >
          AI-Powered Front Office Automation
        </div>

        <h1 className="text-4xl md:text-6xl font-extrabold text-white leading-tight mb-6">
          Stop Losing Leads<br />
          <span style={{ color: "#4B8FE2" }}>After Hours</span>
        </h1>

        <p className="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-10 leading-relaxed">
          Triagent handles your front office 24/7 with AI. Chat with patients, qualify leads,
          book appointments, and triage inquiries -- automatically, while you sleep.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <a
            href="#demo-chat"
            className="px-8 py-4 rounded-xl font-semibold text-white text-base transition-all hover:opacity-90"
            style={{ backgroundColor: "#4B8FE2" }}
          >
            See Live Demo
          </a>
          <a
            href="#contact"
            className="px-8 py-4 rounded-xl font-semibold text-base border-2 border-white text-white transition-all hover:bg-white hover:text-blue-900"
          >
            Book a Discovery Call
          </a>
        </div>

        <div className="mt-16 grid grid-cols-3 gap-8 max-w-lg mx-auto">
          {[
            { value: "24/7", label: "Always on" },
            { value: "3 min", label: "Avg response" },
            { value: "83%+", label: "Gross margin" },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <div className="text-3xl font-extrabold text-white">{stat.value}</div>
              <div className="text-sm text-blue-200 mt-1">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
