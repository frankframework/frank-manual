describe('Tests of frank-manual config', () => {
  it('Test that there are no alerts in the status page', () => {
    cy.visit('')
    // cy.get('[data-cy-status-alert]').should('have.length', 0)
    cy.get('.alert-warning').should('have.length', 0)
  })
})