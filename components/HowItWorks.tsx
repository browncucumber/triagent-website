const steps = [
  {
    number: "01",
    title: "We deploy in one day",
    description:
      "Triagent configures your AI stack, connects it to your existing tools, and deploys to your domain. No IT team required on your end.",
  },
  {
    number: "02",
    title: "AI handles your front office",
    description:
      "Chat answers questions, intake processes new patients, triage routes every inquiry -- automatically, 24/7, from day one.",
  },
  {
    number: "03",
    title: "You see results immediately",
    description:
      "Track every lead, appointment, and response in your dashboard. Most practices recover the setup fee within the first month.",
  },
];

export default function HowItWorks() {
  return (
    <section id="how-it-works" className="py-24 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
            Up and Running in 24 Hours
          </h2>
          <p className="text-lg text-gray-500 max-w-xl mx-auto">
            No lengthy implementations. No IT projects. We handle everything.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-10">
          {steps.map((step) => (
            <div key={step.number} className="text-center">
              <div
                className="w-14 h-14 rounded-2xl flex items-center justify-center text-lg font-extrabold text-white mx-auto mb-5"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                {step.number}
              </div>
              <h3 className="text-lg font-bold mb-3" style={{ color: "#1B2A4A" }}>{step.title}</h3>
              <p className="text-gray-500 text-sm leading-relaxed">{step.description}</p>
            </div>
          ))}
        </div>

        <div
          className="mt-16 rounded-2xl p-8 md:p-12 text-center"
          style={{ background: "linear-gradient(135deg, #1B2A4A 0%, #2E5FA3 100%)" }}
        >
          <h3 className="text-2xl md:text-3xl font-extrabold text-white mb-4">
            Built for practices with no IT staff
          </h3>
          <p className="text-blue-100 max-w-xl mx-auto mb-8">
            Dental, law, med spa, veterinary, accounting. If you have a front desk and a phone, Triagent can automate it.
          </p>
          <a
            href="#contact"
            className="inline-block px-8 py-4 rounded-xl font-semibold text-white border-2 border-white transition-all hover:bg-white hover:text-blue-900"
          >
            Book a Free Discovery Call
          </a>
        </div>
      </div>
    </section>
  );
}
