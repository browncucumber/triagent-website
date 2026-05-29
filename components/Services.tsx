const services = [
  {
    icon: "💬",
    title: "AI Website Chat & 24/7 Answering",
    tagline: "Never miss a lead again",
    description:
      "An intelligent chat widget answers questions, captures lead info, and books appointments around the clock -- even when your office is closed.",
    features: ["24/7 availability", "Lead capture & qualification", "Appointment booking", "Handoff to staff"],
    price: "$397-697/mo",
    setup: "$1,500 setup",
    href: "#demo-chat",
  },
  {
    icon: "📋",
    title: "AI Intake & Appointment Automation",
    tagline: "Zero-touch new patient onboarding",
    description:
      "Smart forms collect information, AI qualifies the lead, and appointments are booked and confirmed via SMS -- no staff required.",
    features: ["Smart intake forms", "SMS confirmations", "Calendar integration", "Insurance pre-screening"],
    price: "$497-797/mo",
    setup: "$2,000 setup",
    href: "#demo-intake",
  },
  {
    icon: "🎯",
    title: "AI Customer Triage & Response Agent",
    tagline: "Every inquiry handled in minutes",
    description:
      "AI reads every inbound email and SMS, classifies urgency, drafts the right response, and escalates only what needs human attention.",
    features: ["Email & SMS triage", "4-category classification", "Auto-draft responses", "Escalation rules"],
    price: "$497-797/mo",
    setup: "$2,000 setup",
    href: "#demo-triage",
  },
];

export default function Services() {
  return (
    <section id="services" className="py-24 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
            Three Services. One Mission.
          </h2>
          <p className="text-lg text-gray-500 max-w-2xl mx-auto">
            Built for dental, law, med spa, vet, and accounting practices with 10-80 staff and no internal IT team.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {services.map((s) => (
            <div
              key={s.title}
              className="rounded-2xl border border-gray-100 p-8 flex flex-col hover:shadow-lg transition-shadow"
              style={{ background: "#FAFBFF" }}
            >
              <div className="text-4xl mb-4">{s.icon}</div>
              <div className="text-xs font-semibold uppercase tracking-wide mb-2" style={{ color: "#2E5FA3" }}>
                {s.tagline}
              </div>
              <h3 className="text-xl font-bold mb-3" style={{ color: "#1B2A4A" }}>{s.title}</h3>
              <p className="text-gray-500 text-sm leading-relaxed mb-6">{s.description}</p>

              <ul className="space-y-2 mb-8 flex-1">
                {s.features.map((f) => (
                  <li key={f} className="flex items-center gap-2 text-sm text-gray-600">
                    <span style={{ color: "#2E5FA3" }}>&#10003;</span> {f}
                  </li>
                ))}
              </ul>

              <div className="border-t border-gray-100 pt-4">
                <div className="text-sm text-gray-400 mb-1">{s.setup}</div>
                <div className="text-lg font-bold mb-4" style={{ color: "#1B2A4A" }}>{s.price} retainer</div>
                <a
                  href={s.href}
                  className="block text-center px-4 py-2.5 rounded-lg text-sm font-semibold text-white transition-opacity hover:opacity-90"
                  style={{ backgroundColor: "#2E5FA3" }}
                >
                  Try Live Demo
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
