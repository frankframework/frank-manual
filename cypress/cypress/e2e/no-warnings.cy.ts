describe('Tests of frank-manual config - no warnings', () => {
  it('Test that there are no alerts in the status page', () => {
    cy.visit('')
    // cy.get('[data-cy-status-alert]').should('have.length', 0)
    cy.tryToFindMoreThanZero('[data-cy-status-alert]', 10)
  })
})