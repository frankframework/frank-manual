describe('Check that expected Frank configurations are really loaded', () => {
  it('Check that expected Frank configurations are really loaded', () => {
    cy.visitConsideringAuth('')
    // Should be passed as array already
    const expectedConfigs = Cypress.env('expectedFrankConfigs')
    for (const expectedConfig of expectedConfigs) {
      cy.get('[data-cy="tab-list__nav-tabs"]').contains(`${expectedConfig}`)
      // Wait to have a screenshot in the video
      cy.wait(1000)
    }
  })
})