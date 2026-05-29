"use client";
import { useState } from "react";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";
type Step = "form" | "submitting" | "success";

export default function DemoIntake() {
  const [step, setStep] = useState<Step>("form");
  const [aiReply, setAiReply] = useState<string>("");
  const [form, setForm] = useState({ name: "", phone: "", service: "", date: "" });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStep("submitting");
    if (!BACKEND_URL) {
      setTimeout(() => setStep("success"), 2000);
      return;
    }
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 60000);
      const res = await fetch(`${BACKEND_URL}/webhook/demo-intake`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
        signal: controller.signal,
      });
      clearTimeout(timeoutId);
      const data = await res.json();
      console.log("n8n response:", JSON.stringify(data));
      if (data.reply) setAiReply(data.reply);
    } catch {}
    setStep("success");
  };

  const reset = () => {
    setStep("form");
    setForm({ name: "", phone: "", service: "", date: "" });
    setAiReply("");
  };

  return (
    <section id="demo-intake" className="py-24 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
            {step === "form" && (
              <>
                <div className="text-sm font-semibold mb-1" style={{ color: "#2E5FA3" }}>
                  Demo Dental Practice -- New Patient Intake
                </div>
                <h3 className="text-xl font-bold mb-6" style={{ color: "#1B2A4A" }}>Request an Appointment</h3>
                <form onSubmit={handleSubmit} className="space-y-4">
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Full Name</label>
                    <input
                      required type="text" value={form.name}
                      onChange={(e) => setForm({ ...form, name: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400"
                      placeholder="Jane Smith"
                    />
                  </div>
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Phone Number</label>
                    <input
                      required type="tel" value={form.phone}
                      onChange={(e) => setForm({ ...form, phone: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400"
                      placeholder="(555) 123-4567"
                    />
                  </div>
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Service Needed</label>
                    <select
                      required value={form.service}
                      onChange={(e) => setForm({ ...form, service: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400 bg-white"
                    >
                      <option value="">Select a service...</option>
                      <option>New patient exam</option>
                      <option>Cleaning</option>
                      <option>Emergency visit</option>
                      <option>Cosmetic consultation</option>
                    </select>
                  </div>
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Preferred Date</label>
                    <input
                      type="date" value={form.date}
                      onChange={(e) => setForm({ ...form, date: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400"
                    />
                  </div>
                  <button
                    type="submit"
                    className="w-full py-3 rounded-xl text-sm font-semibold text-white transition-opacity hover:opacity-90"
                    style={{ backgroundColor: "#2E5FA3" }}
                  >
                    Submit Request
                  </button>
                </form>
              </>
            )}

            {step === "submitting" && (
              <div className="flex flex-col items-center justify-center py-16 text-center">
                <div className="text-4xl mb-4 animate-pulse">⚙️</div>
                <h3 className="text-lg font-bold mb-2" style={{ color: "#1B2A4A" }}>Processing your request...</h3>
                <p className="text-sm text-gray-500">AI is qualifying your intake and checking availability</p>
              </div>
            )}

            {step === "success" && (
              <div className="flex flex-col items-center justify-center py-16 text-center">
                <div className="w-16 h-16 rounded-full flex items-center justify-center text-3xl mb-4" style={{ backgroundColor: "#EBF1F8" }}>
                  ✅
                </div>
                <h3 className="text-lg font-bold mb-2" style={{ color: "#1B2A4A" }}>Appointment Requested!</h3>
                {aiReply && <p className="text-sm text-blue-700 font-medium mb-3 px-4 py-3 bg-blue-50 rounded-lg">{aiReply}</p>}
                <p className="text-sm text-gray-500 mb-1">
                  In a live deployment, {form.phone || "your phone"} would receive an SMS confirmation within 60 seconds.
                </p>
                <p className="text-xs text-gray-400">Staff notified. Calendar updated. Zero manual work.</p>
                <button onClick={reset} className="mt-6 text-sm font-semibold" style={{ color: "#2E5FA3" }}>
                  Try again
                </button>
              </div>
            )}
          </div>

          <div>
            <div className="text-xs font-semibold uppercase tracking-wide mb-3" style={{ color: "#2E5FA3" }}>
              Service 2 -- Live Demo
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
              AI Intake &amp; Appointment Automation
            </h2>
            <p className="text-gray-600 leading-relaxed mb-6">
              Fill out the form as if you were a new patient. In a live deployment, submitting triggers an entire
              automated workflow -- AI qualification, SMS confirmation, and calendar booking -- in under 60 seconds.
            </p>
            <ul className="space-y-3">
              {[
                "AI qualifies every lead automatically",
                "SMS confirmation sent within 60 seconds",
                "Syncs with Google Calendar or Cal.com",
                "Staff gets a clean summary, not a raw form",
              ].map((item) => (
                <li key={item} className="flex items-start gap-2 text-sm text-gray-600">
                  <span className="mt-0.5 font-bold" style={{ color: "#2E5FA3" }}>&#10003;</span> {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}
