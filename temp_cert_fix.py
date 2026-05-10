from pathlib import Path
path = Path('Index.html')
text = path.read_text(encoding='utf-8')
start = '  <div class="certs-grid" style="grid-template-columns: repeat(4, 1fr);">'
end = '<!-- Testimonials -->'
idx = text.find(start)
if idx == -1:
    raise SystemExit('start marker not found')
idx2 = text.find(end, idx)
if idx2 == -1:
    raise SystemExit('end marker not found')
replacement = '''  <div class="certs-grid" style="grid-template-columns: repeat(4, 1fr);">
    <div class="cert-card reveal">
      <div class="cert-card-inner">
        <div class="cert-card-front">
          <span class="cert-icon">✓</span>
          <h4>ISO 9001:2015</h4>
          <p>Quality Management System Certification</p>
          <p style="margin-top:12px;font-size:12px;color:var(--text-light);font-weight:600;">Click to view certificate</p>
        </div>
        <div class="cert-card-back">
          <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 400'%3E%3Crect width='600' height='400' fill='%23f9fdf9'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='24' fill='%232d9b57'%3EISO%209001%3A2015%3C/text%3E%3C/svg%3E" alt="ISO 9001:2015 Certificate">
        </div>
      </div>
    </div>
    <div class="cert-card reveal">
      <div class="cert-card-inner">
        <div class="cert-card-front">
          <span class="cert-icon">✓</span>
          <h4>GMP Approval</h4>
          <p>Good Manufacturing Practices Certification</p>
          <p style="margin-top:12px;font-size:12px;color:var(--text-light);font-weight:600;">Click to view certificate</p>
        </div>
        <div class="cert-card-back">
          <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 400'%3E%3Crect width='600' height='400' fill='%23f9fdf9'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='24' fill='%232d9b57'%3EGMP%20Approval%3C/text%3E%3C/svg%3E" alt="GMP Certificate">
        </div>
      </div>
    </div>
    <div class="cert-card reveal">
      <div class="cert-card-inner">
        <div class="cert-card-front">
          <span class="cert-icon">✓</span>
          <h4>CE Compliance</h4>
          <p>Medical Device Compliance Certification</p>
          <p style="margin-top:12px;font-size:12px;color:var(--text-light);font-weight:600;">Click to view certificate</p>
        </div>
        <div class="cert-card-back">
          <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 400'%3E%3Crect width='600' height='400' fill='%23f9fdf9'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='24' fill='%232d9b57'%3ECE%20Compliance%3C/text%3E%3C/svg%3E" alt="CE Compliance Certificate">
        </div>
      </div>
    </div>
    <div class="cert-card reveal">
      <div class="cert-card-inner">
        <div class="cert-card-front">
          <span class="cert-icon">✓</span>
          <h4>Combined Certificate</h4>
          <p>Single two-page certification entry</p>
          <p style="margin-top:12px;font-size:12px;color:var(--text-light);font-weight:600;">Click to view both pages</p>
        </div>
        <div class="cert-card-back">
          <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 400'%3E%3Crect width='600' height='400' fill='%23f9fdf9'/%3E%3Ctext x='50%25' y='44%25' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='20' fill='%232d9b57'%3ETwo-Page%20Certificate%3C/text%3E%3Ctext x='50%25' y='56%25' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='16' fill='%232d9b57'%3EPages%201%20%26%202%3C/text%3E%3C/svg%3E" alt="Two-Page Certificate">
        </div>
      </div>
    </div>
  </div>
</section>

<div id="cert-modal" class="cert-modal" aria-hidden="true">
  <div class="cert-modal-box">
    <button class="cert-modal-close" type="button" onclick="closeCertModal()" aria-label="Close certificate preview">×</button>
    <img id="cert-modal-image" class="cert-modal-image" src="" alt="Certificate">
  </div>
</div>

<div id="site-lightbox" class="site-lightbox" aria-hidden="true" onclick="handleLightboxBackdrop(event)">
  <div class="site-lightbox-content" role="dialog" aria-modal="true" aria-label="Image preview">
    <button class="site-lightbox-close" type="button" onclick="closeSiteLightbox()" aria-label="Close image preview">×</button>
    <img id="site-lightbox-image" src="" alt="">
    <div class="site-lightbox-title" id="site-lightbox-title"></div>
  </div>
</div>

''' + end
text = text[:idx] + replacement + text[idx2:]
path.write_text(text, encoding='utf-8')
print('patched')
