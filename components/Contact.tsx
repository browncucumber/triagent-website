export default function Contact() {
  return (
    <section id="contact" className="py-24 px-6" style={{ background: "#EBF1F8" }}>
      <div className="max-w-3xl mx-auto text-center">
        <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
          Ready to Automate Your Front Office?
        </h2>
        <p className="text-gray-600 mb-10 text-lg">
          Book a free 30-minute discovery call. We will show you exactly how Triagent works for your practice
          and give you a clear cost and timeline.
        </p>

        <div className="bg-white rounded-2xl shadow-xl p-8 md:p-12">
          <div className="grid md:grid-cols-2 gap-6 mb-6">
            <div className="rounded-xl p-6 text-left" style={{ background: "#EBF1F8" }}>
              <div className="text-2xl mb-3">📞</div>
              <h3 className="font-bold mb-1" style={{ color: "#1B2A4A" }}>Book a Call</h3>
              <p className="text-sm text-gray-500 mb-4">30 minutes. No sales pressure. We figure out if this is a fit.</p>
              <a
                href="mailto:hello@triagent.cloud?subject=Discovery Call Request"
                className="inline-block px-5 py-2.5 rounded-lg text-sm font-semibold text-white transition-opacity hover:opacity-90"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                Email to Schedule
              </a>
            </div>
            <div className="rounded-xl p-6 text-left" style={{ background: "#EBF1F8" }}>
              <div className="text-2xl mb-3">✉️</div>
              <h3 className="font-bold mb-1" style={{ color: "#1B2A4A" }}>Send a Message</h3>
              <p className="text-sm text-gray-500 mb-4">Questions about pricing, services, or your specific use case.</p>
              <a
                href="mailto:hello@triagent.cloud"
                className="inline-block px-5 py-2.5 rounded-lg text-sm font-semibold border-2 transition-colors"
                style={{ color: "#2E5FA3", borderColor: "#2E5FA3" }}
              >
                hello@triagent.cloud
              </a>
            </div>
          </div>
          <p className="text-xs text-gray-400">
            Typical response within 2 business hours. Based in the US. Serving professional practices nationwide.
          </p>
        </div>
      </div>
    </section>
  );
}
