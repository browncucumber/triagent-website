"use client";
import { useState, useRef, useEffect } from "react";

interface Message {
  role: "user" | "assistant";
  content: string;
}

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";

export default function DemoChat() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Hi! I am the AI assistant for Triagent Demo Dental. How can I help you today? I can answer questions about our services, hours, insurance, and help you book an appointment.",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg: Message = { role: "user", content: input.trim() };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    if (!BACKEND_URL) {
      setTimeout(() => {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content:
              "This is a demo placeholder. The live AI backend will be connected once the Oracle VM is configured. You would see real AI responses here powered by Ollama running on a local GPU server.",
          },
        ]);
        setLoading(false);
      }, 1000);
      return;
    }

    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 60000);
      const res = await fetch(`${BACKEND_URL}/webhook/demo-chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMsg.content, history: messages }),
        signal: controller.signal,
      });
      clearTimeout(timeoutId);
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "assistant", content: data.reply || data.response || "No response received." }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Sorry, I am having trouble connecting right now. Please try again shortly." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="demo-chat" className="py-24 px-6" style={{ background: "#EBF1F8" }}>
      <div className="max-w-6xl mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div>
            <div className="text-xs font-semibold uppercase tracking-wide mb-3" style={{ color: "#2E5FA3" }}>
              Service 1 -- Live Demo
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
              AI Website Chat &amp; 24/7 Answering
            </h2>
            <p className="text-gray-600 leading-relaxed mb-6">
              This is the exact chat widget your clients get on their website. It answers patient questions,
              captures contact info, and books appointments -- 24 hours a day. Try it yourself.
            </p>
            <ul className="space-y-3">
              {[
                "Powered by local Ollama AI -- no data leaves your network",
                "Customized with your clinic name, services, and hours",
                "Escalates to staff when needed",
                "Captures every lead even at 2am",
              ].map((item) => (
                <li key={item} className="flex items-start gap-2 text-sm text-gray-600">
                  <span className="mt-0.5 font-bold" style={{ color: "#2E5FA3" }}>&#10003;</span> {item}
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-white rounded-2xl shadow-xl overflow-hidden flex flex-col" style={{ height: "480px" }}>
            <div className="px-5 py-4 flex items-center gap-3 border-b" style={{ backgroundColor: "#1B2A4A" }}>
              <div
                className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold text-white"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                T
              </div>
              <div>
                <div className="text-sm font-semibold text-white">Triagent Assistant</div>
                <div className="flex items-center gap-1.5">
                  <div className="w-1.5 h-1.5 rounded-full bg-green-400" />
                  <span className="text-xs text-gray-300">{BACKEND_URL ? "Live" : "Demo mode"}</span>
                </div>
              </div>
            </div>

            <div className="flex-1 overflow-y-auto p-4 space-y-3" style={{ background: "#F8FAFF" }}>
              {messages.map((m, i) => (
                <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                  <div
                    className="max-w-xs px-4 py-2.5 rounded-2xl text-sm leading-relaxed"
                    style={
                      m.role === "user"
                        ? { backgroundColor: "#2E5FA3", color: "white" }
                        : { backgroundColor: "white", color: "#1B2A4A", border: "1px solid #E5E9F0" }
                    }
                  >
                    {m.content}
                  </div>
                </div>
              ))}
              {loading && (
                <div className="flex justify-start">
                  <div className="px-4 py-2.5 rounded-2xl bg-white border border-gray-200 text-sm text-gray-400">
                    Typing...
                  </div>
                </div>
              )}
              <div ref={bottomRef} />
            </div>

            <div className="p-3 border-t bg-white flex gap-2">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                placeholder="Type a message..."
                className="flex-1 text-sm px-4 py-2.5 rounded-xl border border-gray-200 outline-none focus:border-blue-400"
              />
              <button
                onClick={sendMessage}
                disabled={loading || !input.trim()}
                className="px-4 py-2.5 rounded-xl text-sm font-semibold text-white disabled:opacity-50 transition-opacity hover:opacity-90"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                Send
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
