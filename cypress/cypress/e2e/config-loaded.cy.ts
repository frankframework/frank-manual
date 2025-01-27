describe('Check that expected Frank configurations are really loaded', () => {
  it('Check that expected Frank configurations are really loaded', () => {
    cy.visit('')
    const expectedConfigs = Cypress.env('expectedFrankConfigs').split(',')
    for (const expectedConfig of expectedConfigs) {
      cy.get(`[data-cy-select-tab=${expectedConfig}]`)
      // Wait to have a screenshot in the video
      cy.wait(1000)
    }
  })
})